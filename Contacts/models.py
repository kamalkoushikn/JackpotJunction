from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    created_at = models.TimeField(auto_now=False, auto_now_add=False)