from django.db import models
from django.contrib.auth import get_user_model

class Movie(models.Model):
    name=models.CharField(max_length=255)
    publisher=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Genre=models.CharField(max_length=255)
    global_assessment=models.CharField(max_length=255)
    duration=models.IntegerField()
    
    def __str__(self):
        return self.name

