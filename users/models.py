from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class Client(AbstractUser):
    is_Client = models.BooleanField(default=False)
    is_Internal = models.BooleanField(default=False)

class Internal(models.Model):
    Client = models.OneToOneField(Client,related_name = 'PBuser', on_delete=models.CASCADE, primary_key=True)
