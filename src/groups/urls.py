from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('create/', views.create_group, name='create_group'),
    path('details/<slug>/', views.group_details, name='group_details'),
    path('delete/<slug>/', views.delete_group, name='delete_group')
]
