from django.db import models
from users.models import Profile
import uuid


    
class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True, editable = False)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    owner = models.ForeignKey(Profile,null = True,blank = True , on_delete=models.SET_NULL)
    title = models.CharField(max_length = 200)
    tags = models.ManyToManyField(Tag,blank=True)
    vote_total = models.IntegerField(default = 0, null = True,blank = True)
    featured_image = models.ImageField(null=True,blank=True,default="default.jpg")
    vote_ratio = models.IntegerField(default = 0, null = True,blank = True)
    description = models.TextField(null = True,blank = True)
    demo_link = models.CharField(max_length = 200,null = True,blank = True)
    source_link = models.CharField(max_length = 200,null = True,blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True, editable = False)
    
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up','UP VOTE'),
        ('down','DOWN VOTE')
    )
    # owner = 
    project = models.ForeignKey(Project,on_delete = models.CASCADE)
    body = models.TextField(null = True,blank = True)
    value = models.CharField(max_length = 200,choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True, editable = False)
    
    
    def __str__(self):
        return self.value
    

    
    
        
    

    
