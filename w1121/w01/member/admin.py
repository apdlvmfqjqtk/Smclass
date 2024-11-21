from django.contrib import admin
from member.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id','name','nicName','mdate']

# 관리자 페이지 컬럼
# admin.site.register(Member,MemberAdmin)