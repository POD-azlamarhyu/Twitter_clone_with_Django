from django.contrib import admin
from .models import *
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    save_on_top =True
    search_fields = ["id","text","user__email","user__username","images"]

admin.site.register(Tweet,TweetAdmin)
