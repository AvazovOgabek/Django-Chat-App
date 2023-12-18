from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(
        upload_to='profile_images',
        default='Unknown.jpeg',
    )
    
    def __str__(self):
        return f'{self.user.username} Profile'
