from django.db import models
from datetime import datetime

class Member(models.Model):
  id = models.CharField(max_length=20, primary_key=True)
  pw = models.CharField(max_length=20, null=False)
  name = models.CharField(max_length=20)
  nicName = models.CharField(max_length=50)
  tel = models.CharField(max_length=50, default='010-0000-0000')
  gender = models.CharField(max_length=10, default='남자')
  hobby = models.CharField(max_length=50, default='book')
  mdate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.id},{self.name},{self.gender},"