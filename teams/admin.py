from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([ Team, Manager, Coach, TeamRequest])
