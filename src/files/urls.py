from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('delete/<name>/', views.delete_file, name='delete_file'),

]
