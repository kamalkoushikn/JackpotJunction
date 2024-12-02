from django.db import models
# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False,unique=True)
    email = models.EmailField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)