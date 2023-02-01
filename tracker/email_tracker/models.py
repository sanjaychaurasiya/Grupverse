from django.db import models


# Create your models here.
class Users(models.Model):
    """Class to models for users"""
    email = models.EmailField(max_length=255, blank=False, unique=True)
    status = models.BooleanField(default=False)
    count = models.PositiveIntegerField(default=0)
    data_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

