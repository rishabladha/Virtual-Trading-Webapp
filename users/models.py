from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10, default="")
    pan = models.CharField(max_length=10, default="")
    image = models.ImageField(
        default='default_profile_image.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 256 or img.width > 256:
            output_size = (256, 256)
            img.thumbnail(output_size)
            img.save(self.image.path)
