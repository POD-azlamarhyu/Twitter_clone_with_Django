from django.contrib import admin
from .models import Profiles
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UA
# Register your models here.

# class ProfileInline(admin.StackedInline):
#     model = Profiles
#     max_num = 1
#     can_delete = False

# class UserAdmin(UA):
#     inlines = [ProfileInline]

admin.site.register(Profiles)
