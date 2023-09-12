from django.contrib import admin
from .models import Player, PlayerRating, Position

# Register your models here.
admin.site.register([ PlayerRating, Player, Position ])
