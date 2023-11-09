from django.contrib import admin

from .models import Diary, DiaryCommit, DiaryComment


admin.site.register(Diary)
admin.site.register(DiaryCommit)
admin.site.register(DiaryComment)

