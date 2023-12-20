from django.db import models
from django.conf import settings

class New(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, )
    
    def __str__(self): 
        return self.title