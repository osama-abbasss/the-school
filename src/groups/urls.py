from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [

    path('create/', views.create_group, name='create_group'),
    path('details/<slug>/', views.group_details, name='group_details'),
    path('delete/<slug>/', views.delete_group, name='delete_group'),
    path('join/<slug>/', views.join_group, name='join_group'),
    path('leave/<slug>/', views.leave_group, name='leave_group'),
    path('remove/<slug>/<username>', views.remove_member, name='remove_member'),

]
