from django.db import models
from django.contrib.auth.models import AbstractUser


class State(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

COACH_ROLE = Role.objects.get_or_create(name='Coach')
MANAGER_ROLE = Role.objects.get_or_create(name='Manager')
OWNER_ROLE = Role.objects.get_or_create(name='Owner')

class UserAccount(AbstractUser):
    roles = models.ManyToManyField(Role)
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.get_full_name()

    def can_create_team(self):
        return ( 
            (COACH_ROLE in self.roles) 
            or (MANAGER_ROLE in self.roles) 
            or (OWNER_ROLE in self.roles)
        )

    