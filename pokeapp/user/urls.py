from . import views
from django.urls import path 


urlpatterns = [
    path('login/', views.login, name='loginpage'),
    path('register/', views.register, name='registerpage'),
]