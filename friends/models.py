from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile_class(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='mahi')


class Frined_request_class(models.Model):
    User = models.CharField(max_length=75)
    Request_user = models.CharField(max_length=75)
    Pending = models.CharField(max_length=10)
    Accept = models.CharField(max_length=10)
    Decline = models.CharField(max_length=10)

    def __str__(self):
        return self.User
