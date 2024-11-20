from django.db import models

class Member(models.Model):
  id = models.CharField(max_length=100, primary_key=True) # id를 프라이머리 키로 삼겠다
  pw = models.CharField(max_length=100, blank=False)      # 빈칸 허용 안함
  name = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nicname = models.CharField(max_length=100)
  cdate = models.DateTimeField(auto_now=True)             # 자동으로 현재 시간 입력

  def __str__(self):
    return f"{self.id},{self.name}"