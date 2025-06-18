from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('my-login', views.my_login, name="my-login"),
]