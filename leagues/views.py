from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
import datetime
from django.http import JsonResponse


def team_data(team):
    return { 'name': team.name, 'short_name': team.short_name}
#   GENERATE TOURNAMENT / LEAGUE FIXTURES

def generate_fixtures(teams, competition_type):
    pass


#   REGISTER TEAM FOR TOURNAMENT
@api_view(['POST'])
def register_team(request):
    pass


@api_view(['POST'])
def request_player_to_join_team(request):
    pass


@api_view(['GET'])
def get_today_fixtures(request):
    matches = Match.objects.filter(date__day=datetime.date.today().day)
    #print("MATCHES : ", matches)
    status = 200

    
    return JsonResponse({
        'status': status,
        'body': {
            'fixtures': [
                        { 
                            'home_team': team_data(match.home_team),
                          'away_team': team_data(match.away_team),
                          'date': match.date,
                          'kick_off_time': match.date.time()
                        }
                        for match in matches 
            ]
        }
    })


@api_view(['GET'])
def get_all_fixtures(request):  #   INDEX RESPONSE BY DATES
    matches = Match.objects.all()
    status = 200

    return JsonResponse({
        'status': status,
        'body': {
            'fixtures': [
                        { 'home_team': match.home_team.name,
                          'away_team': match.away_team.name,
                          'date': match.date,
                          'kick_off_time': match.date.time()
                        }
                        for match in matches 
            ]
        }
    })
