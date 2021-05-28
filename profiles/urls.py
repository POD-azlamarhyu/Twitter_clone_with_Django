from django.urls import path
from .views import profileEditView,profileView

app_name = "profiles"
urlpatterns=[
    path('profile_detail/',profileView,name='profile_detail'),
    path('profile_edit/',profileEditView,name='profile_edit'),
]