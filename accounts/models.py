from django.db import models
from django.contrib.auth.models import User
from base.models import Basemodel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.email import send_account_activation_email


# Create your models here.


class Profile(Basemodel):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank= True)

class Profile_img(Basemodel):
    user= models.ForeignKey("Profile", on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile')


@receiver(post_save, sender= User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            email = instance.email 
            Profile.objects.create(user= instance, email_token=email_token )
            send_account_activation_email(email, email_token)
    except Exception as E:
        print(E)
            