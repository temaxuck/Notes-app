from django.db import models
from django.contrib.auth.models import User
import os

def get_upload_path(instance, filename):
    return os.path.join('profile_img', str(instance.user.id), str(filename))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=os.path.join('profile_img', 'default.png'), upload_to=get_upload_path)
    
    def __str__(self):
        return f'{self.user.username} Profile'
