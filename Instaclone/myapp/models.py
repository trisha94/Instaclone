import uuid

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    has_verified_mobile = models.BooleanField(default=False)
    created_On = models.DateTimeField(auto_now_add=True)




class SessionToken(models.Model):

  user = models.ForeignKey(User)
  session_token = models.CharField(max_length=255)
  created_on = models.DateTimeField(auto_now_add=True)
  is_valid = models.BooleanField(default=True)

  def create_token(self):
      self.session_token = uuid.uuid4()
