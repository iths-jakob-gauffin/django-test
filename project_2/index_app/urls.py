from django.urls import path
from . import views

# Template tagging
app_name = 'index_app'

urlpatterns = [
    path('', views.index),
    path('help/', views.help, name="help"),
    path('bild/', views.bild, name="bild"),
    path('users/', views.users, name="users"),
    path('create_user/', views.create_user, name='create_user'),
]
