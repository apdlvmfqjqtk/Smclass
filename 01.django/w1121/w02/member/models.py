from django.db import models

class Member(models.Model):
  name = models.CharField(max_length=100)
  id = models.CharField(max_length=100, primary_key=True)
  pw = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  tel = models.CharField(max_length=30)
  birth = models.CharField(max_length=50)
  gender = models.CharField(max_length=5, default='남성')
  news = models.CharField(max_length=5, default='예')
  sms = models.CharField(max_length=5, default='예')

  # 분양회원
  memnum = models.CharField(max_length=8)
  memaaa = models.IntegerField(max_length=4)

  # 선택정보
  job = models.CharField(max_length=10)
  married = models.CharField(max_length=5)
  hobby = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.name}, {self.id}, {self.pw}"
