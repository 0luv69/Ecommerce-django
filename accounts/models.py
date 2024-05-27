from django.db import models
from django.contrib.auth.models import User
from base.models import Basemodel




# Create your models here.


class Profile(Basemodel):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank= True)

class Profile_img(Basemodel):
    user= models.ForeignKey("Profile", on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile')