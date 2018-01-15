from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Lightning(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50, default='')
    message = models.TextField()


class Comment(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    directed_to = models.ForeignKey(Lightning, on_delete=models.CASCADE, null=True)
    message = models.TextField()


