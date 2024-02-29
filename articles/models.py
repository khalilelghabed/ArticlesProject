from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    auteur=models.ForeignKey(User,on_delete=models.CASCADE,related_name='article')
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_publication=models.DateField(auto_now_add=True)

    
# Create your models here.
