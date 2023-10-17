from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN ='ADMIN', 'admin'
        STUDENT = 'STUDENT','student'
 
    base_role = Role.Admin

    role = models. CharField(max_length=50, choices= Role.choices)

    def save(self, *args,**kwargs):
        if not self.pk:
            self.role =self.base_role
            return super().save