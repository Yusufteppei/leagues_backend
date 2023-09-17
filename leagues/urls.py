from django.urls import path
from .views import *


urlpatterns = [
    path('get-today-fixtures', get_today_fixtures, name='get_today_fixtures'),
    path('get-all-fixtures', get_all_fixtures, name='get_all_fixtures'),
    path('get-current-competitions', get_current_competitions, name='get_current_competitions'),
    path('get-all-competitions', get_all_competitions, name='get_all_competitions')
]
