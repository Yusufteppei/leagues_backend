from django.db import models
from authentication.models import UserAccount
from players.models import Player


class Owner(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.get_full_name()


# CAN REMOVE COACH
class Manager(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.get_full_name()


class Coach(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.account.get_full_name()

    class Meta:
        verbose_name_plural = "Coaches"
        
        
class Team(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, blank=True)
    motto = models.CharField(max_length=64, null=True, blank=True)
    logo = models.ImageField(upload_to="team_logos", null=True, blank=True)
    short_name = models.CharField(max_length=4)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name


class TeamRequest(models.Model):
    requesting_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    requested_player = models.ForeignKey(Player, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.requesting_team} ----> {self.requested_player}"
