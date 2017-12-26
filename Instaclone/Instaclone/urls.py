from django.conf.urls import include

from django.conf.urls import url
from django.contrib import admin
from dashboard import views

urlpatterns = [
    url(r'^$', 'Instaclone.views.home', name='home'),
     url(r'^blog/', include('blog.urls')),
    url(r'^$', views.FeedView),
    url(r'^login/', views.LoginView),
    url(r'^signup/', views.SignupView),
    url(r'^post/', views.PostView),
    url(r'^like/', views.LikeView),
    url(r'^comment/', views.CommentView),
    url(r'^profile/$', views.ProfileView),
    url(r'^logout/$', views.LogoutView),
    url(r'^admin/', admin.site.urls),
]

