from django.db import models

class Member(models.Model):
  id = models.CharField(max_length=20, primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  nicName = models.CharField(max_length=50)
  tel = models.CharField(max_length=50, default='010-1111-1111')
  gender = models.CharField(max_length=10, default='남자')
  hobby = models.CharField(max_length=50, default='game')
  mdate = models.DateTimeField(auto_now=True)  # auto_now_add : 입력할 때 시간값만 들어가고 수정 한 시간은 안들어감

  def __str__(self):
    return f"{self.id},{self.name},{self.nicName}"