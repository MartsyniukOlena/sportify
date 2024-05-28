from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Contact Request from {self.name}'