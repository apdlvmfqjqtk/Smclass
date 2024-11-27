from django.db import models
from member.models import Member

class Board(models.Model):
  no = models.AutoField(primary_key=True)

  # Member table에서 가져와서 bno의 foregin키로 설정 DO.NOTHING(포리즌키가 삭제되더라도 member는 남김)
  member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True) # 작성자
  title = models.CharField(max_length=50) # 제목
  content = models.TextField()            # 내용
  hit = models.IntegerField(default=0)    # 조회수
  date = models.DateField(auto_now=True)  # 작성 시각
  
  # 이미지 파일 삽입 변수
  file = models.ImageField(null=True, upload_to='board', height_field=300)  # , width_field=None, max_length=None

  # 계층형 계시판 생성에 필요한 변수들
  group = models.IntegerField(null=True)  # 글 답글 묶음
  step = models.IntegerField(default=0)   # 답글 배치 순서 위한 변수
  indent = models.IntegerField(default=0) # 들여쓰기 위한 변수

  def __str__(self):
    return f"{self.no},{self.title},{self.group},{self.date}"