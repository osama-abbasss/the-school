from django.urls import path
from . import views

app_name = 'covid_19'

urlpatterns = [
    path('', views.all_counties, name='all_counties'),
    path('<slug>/', views.single_country, name='single')
]
