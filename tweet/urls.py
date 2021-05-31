from django.urls import path
from .views import *

urlpatterns = [
    path('tweet/<int:tweet_id>',tweetDetailView,name="tweetdetail"),
    path('tweet/',tweetListView,name="tweetlist"),
    path('tweet/create/',tweetCreateView,name="tweetcreate"),
]