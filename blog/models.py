from django.db import models
from django.utils import timezone

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True,blank=False)
    password=models.CharField(max_length=15)

    
    def __unicode__(self):
        return self.email

class UserEditPro(models.Model):
    user=models.OneToOneField(Register, unique=True)
    name=models.CharField(max_length=30)
    bio=models.TextField(null=True,blank=True)
    contect=models.CharField(max_length=15,null=True,blank=True)

    def __unicode__(self):
        return self.user

class Post(models.Model):
    author = models.ForeignKey(Register)
    title=models.CharField(max_length=50)
    body=models.TextField(null=True,blank=True)
    published_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
