from django.db import models

# Create your models here.
class Mypage(models.Model):
    member_id = models.CharField(max_length=45, default='')
    timetable = models.CharField(max_length=200, default='')
    keyword = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=45, default='')
    