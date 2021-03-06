from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank = True, null = True)
    avatar = models.URLField(blank = True, null = True)
    
    pass

    def __str__(self):
        return self.username