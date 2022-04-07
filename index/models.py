from distutils.command.upload import upload
from django.db import models

# Create your models here.

class repo(models.Model):
    
    title = models.CharField(max_length=150)
    mindes = models.CharField(max_length=200)
    image = models.CharField(max_length=500,default="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
    urls = models.CharField(max_length=200,default='#')

           
class certificate(models.Model):
    
    title = models.CharField(max_length=150)
    mindes = models.TextField(max_length=600)
    image = models.CharField(max_length=600)
    by = models.TextField(max_length=600)
    url = models.CharField(max_length=200,default='#')
    

   