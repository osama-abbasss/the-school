from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_view, name='profile_form'),
    path('activate/<code>/', views.account_activated, name='activate'),
]
