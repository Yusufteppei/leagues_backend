from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from authentication.models import *


class Position(models.Model):
    short_name = models.CharField(max_length=8)
    full_name = models.CharField(max_length=64)

    def __str__(self):
        return self.short_name


class Player(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, null=True, blank=True)
    positions = models.ManyToManyField(Position)
    preferred_numbers = ""

    def __str__(self):
        return self.nickname


class PlayerRating(models.Model):
    voter = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="voting_player")
    votee = models.ForeignKey(Player, on_delete=models.CASCADE)
    value = models.IntegerField(
        default=50,
        validators=[ MinValueValidator(0), MaxValueValidator(99) ]
    )

    def __str__(self):
        return f"{self.voter}'s rating for {self.votee}"
