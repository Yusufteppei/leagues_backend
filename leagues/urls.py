from django.urls import path
from .views import *


urlpatterns = [
    path('get-today-fixtures', get_today_fixtures, name='get_today_fixtures'),
    path('get-all-fixtures', get_all_fixtures, name='get_all_fixtures')
]
