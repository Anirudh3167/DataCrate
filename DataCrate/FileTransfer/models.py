from django.db import models

# Create your models here.
class FileLinks(models.Model):
    code = models.CharField(max_length = 8, primary_key = True)
    path = models.FilePathField()
    