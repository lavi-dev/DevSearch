from django.db import models
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
import uuid


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,blank = True)
    name = models.CharField(max_length=200,null=True) 
    email = models.EmailField(max_length=500,null=True) 
    short_intro = models.CharField(max_length=500,null=True)
    bio = models.TextField(null=True)
    username = models.CharField(max_length=200,null=True,blank=True) 
    location = models.CharField(max_length=200,null=True,blank=True) 
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200,null=True) 
    social_twitter = models.CharField(max_length=200,null=True) 
    social_linkedin= models.CharField(max_length=200,null=True)
    social_website= models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.user)
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True,blank = True)
    created  = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    
    def __str__(self):
        return str(self.name)
    
