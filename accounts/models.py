from django.db import models

from django.db import models

class CustomUser(models.AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)