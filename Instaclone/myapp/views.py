import datetime
import user

from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render

from myapp.models import SessionToken

from forms import SignUpForm, LoginForm


# Create your views here.

def signup_view(request):
   if request.method == "POST":
        form = SignUpForm(request.POST)
       if form.is_valid():
           username = form.cleaned_data['username']
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           # saving data to DB
           user = UserModel(name=name, password=make_password(password), email=email, username=username)
           user.save()
   elif request.method == "GET":
       form = SignUpForm()

   return render(request, 'index.html', {'form': form})

# views.py

def login_view(request):

       if request.method == "POST":
           form = LoginForm(request.POST)
           if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = UserModel.objects.filter(username=username).first()

               if user:
                   # Check for the password
                   if check_password(password, user.password):
                       token = SessionToken(user=user)
                       token.create_token()
                       token.save()
                       print 'User is valid'
                   else:
                       print 'User is invalid'

       elif request.method == "GET":
           form = LoginForm()

       return render(request, 'login.html', {'form': form})


# def login_view(request):
#
#
#     form = LoginForm(request.POST)
#
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = UserModel.objects.filter(username=username).first()
#
#         if user:
#             # Check for the password
#             if check_password(password, user.password):
#                 token = SessionToken(user=user)
#                 token.create_token()
#                 token.save()
#                 print 'User is valid'
#             else:
#                 print 'User is invalid'

def check_validation(request):
  if request.COOKIES.get('session_token'):
    session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
    if session:
      return session.user
  else:
    return None




