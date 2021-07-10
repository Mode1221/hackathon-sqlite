from django.db import models

# Create your models here.
class Member(models.Model):
    member_id = models.CharField(max_length=45, default='')
    password = models.CharField(max_length=45, default='')
    name = models.CharField(max_length=45, default='')
    email = models.EmailField(max_length=45, default='')
