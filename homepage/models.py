from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.content[0:20]
