from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserDetails(AbstractUser):
    # user name, password, first name, last name are abstracted.
    score = models.IntegerField(default=100)
    name = models.CharField(default="", max_length=50)

    def __str__(self):
        return self.username