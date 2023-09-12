from django.contrib import admin
from .models import League, Rules, Competition, Match, Rating
from django.contrib import messages

# Register your models here.

admin.site.site_header = "Leagues Admin"
admin.site.site_title = "Leagues Admin"


admin.site.register([ League, Competition, Rules, Rating ])

@admin.register(Match)
class MatchModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'home_team', 'away_team', 'competition', 'home_team_points', 'away_team_points')
    list_display_links = ('__str__', 'home_team', 'away_team', 'competition')
    list_editable = ('home_team_points', 'away_team_points')
    list_filter = ('competition',)
    list_per_page = 16

    def save_model(self, request, obj, form, change):
        if obj.home_team == obj.away_team:
            messages.warning(request, "A team can not be its own opponent")
        return super().save_model(request, obj, form, change)