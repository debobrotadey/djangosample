from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
# Register your models here.
admin.site.register(Member, MemberAdmin)
# admin.site.register(Member)

# from django.contrib import admin

# Register your models here.
