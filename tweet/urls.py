from django.urls import path
from .views import *

app_name = "tweet"
urlpatterns = [
    path('tweet/<int:tweet_id>',tweetDetailView,name="tweetdetail"),
    path('tweet/',tweetListView,name="tweetlist"),
    path('tweet/create/',tweetCreateView,name="tweetcreate"),
    path('tweet/edit/<int:tweet_id>',tweetEditView,name="tweetedit"),
    path('tweet/delete/<int:tweet_id>',tweetDeleteView,name="tweetdelete"),
]