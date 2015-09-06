from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True,blank=False)
    password=models.CharField(max_length=15)

    
    def __unicode__(self):
        return self.email

class UserEditPro(models.Model):
    user=models.OneToOneField(Register,unique=True)
    name=models.CharField(max_length=30)
    bio=models.TextField(null=True,blank=True)
    contect=models.CharField(max_length=15,null=True,blank=True)

    def __unicode__(self):
        return self.user


