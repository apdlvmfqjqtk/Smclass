from django.db import models

class Member(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  pw = models.CharField(max_length=100, null=False)
  name = models.CharField(max_length=100)
  nicName = models.CharField(max_length=100, null=True)    # 빈공백 들어와도 패스
  mdate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.id},{self.pw},{self.nicName}"