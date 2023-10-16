from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    department = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='static/assets/images/')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

