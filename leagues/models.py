from django.db import models
from teams.models import Team
from players.models import Player
from django.contrib import messages


class League(models.Model):
    name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to="league_logos", null=True, blank=True)

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to="competition_logos", null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{ self.name } - { self.league }" 

    @property
    def is_active(self):
        return True

    @property
    def type(self):
        pass

    @property
    def registered_team_count(self):
        pass

    @property
    def registered_players_count(self):
        pass


class Rules(models.Model):
    competition = models.OneToOneField(Competition, on_delete=models.CASCADE)
    minimum_number_of_players = models.IntegerField()
    maximum_number_of_players = models.IntegerField()
    minimum_number_of_teams = models.IntegerField()
    maximum_number_of_teams = models.IntegerField()
    registration_fees = models.BigIntegerField()
    competition_type = models.CharField(max_length=16, choices=(('Knock Out', 'Knock Out'), ('Ranking', 'Ranking')))
    auto_shuffling = models.BooleanField(default=True)
    match_duration = models.DurationField()
    overtime_duration = models.DurationField()

    extra_description = models.TextField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Rules"


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name = "home_games", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name = "away_games", on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    #date = models.DateField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)


    #   POST GAME
    home_team_points = models.IntegerField(default=0)
    away_team_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.home_team.short_name} v {self.away_team.short_name}"

    class Meta:
        verbose_name_plural = "Matches"


    @property
    def winning_team(self):
        if self.home_team_points > self.away_team_points:
            return self.home_team
        elif self.home_team_points < self.away_team_points:    
            return self.away_team
        else:
            return "tie"

    @property
    def losing_team(self):
        if self.home_team_points < self.away_team_points:
            return self.home_team
        elif self.home_team_points > self.away_team_points:   
            return self.away_team
        else:
            return "tie"


class Rating(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    rating_player = models.ForeignKey(Player, on_delete=models.CASCADE)
    rated_player = models.ForeignKey(Player, related_name="personal_ratings", on_delete=models.CASCADE)
    rating_score = models.IntegerField()



class Award(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    title = models.CharField(max_length=32)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
