from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('',views.TopPage.as_view(),name="base"),
]