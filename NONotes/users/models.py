from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image
import os

def get_upload_path(instance, filename):
    return os.path.join('profile_img', str(instance.user.id), str(filename))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=os.path.join('profile_img', 'default.png'), upload_to=get_upload_path)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
                
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
