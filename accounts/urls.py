from django.urls import path
from .views import LoginViews,LogoutViews,TopPage,UserCreateView,LogoutViews,LogedoutViews
from django.contrib.auth import views as auth_view

app_name='accounts'
urlpatterns = [
    path('',TopPage.as_view(),name="base"),
    path('signup',UserCreateView.as_view(),name="signup"),
    path('login',LoginViews.as_view(),name="login"),
    path('logout',LogoutViews.as_view(),name="logout"),
    path('loggedout',LogedoutViews.as_view(),name="loggedout"),
]