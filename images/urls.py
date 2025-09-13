from . import views
from django.urls import path

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create')
]