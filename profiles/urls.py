from django.urls import path
from .views import ProfileCreateView,ProfileView

app_name = "profiles"
urlpatterns=[
    path('profile/<slug:pk>',ProfileView.as_view(),name='detail'),
    path('profile/myprofile/<slug:pk>',ProfileCreateView.as_view(),name='edit'),
]