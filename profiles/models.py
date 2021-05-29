from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class Profiles(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True,on_delete=models.CASCADE)
    account_id = models.CharField(max_length=255,unique=True)
    location = models.CharField(max_length=220,null=True,blank=True)
    bio = models.TextField(blank=True,null=True)
    timestap = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)
    icon = models.ImageField(upload_to="images",blank=True,null=True)
    header_img = models.ImageField(upload_to="images",blank=True,null=True)
    

    def __str__(self):
        return self.account_id

