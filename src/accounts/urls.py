from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('create/profile/', views.create_profile, name='create_profile'),
    path('edit/profile/', views.edit_profile, name='edit_profile'),
    path('profile/<username>/', views.profile_view, name='profile'),
    path('activate/<code>/', views.account_activated, name='activate'),
]
