from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view

###     COMPETITION VIEWS


#   CAPTAIN OR COACH ACTIONS

@api_view(['POST'])
def create_team(request):   #   

    user = request.user
    if user.can_create_team():

        ##  RAW IDS
        name = request.data['name']
        #   owner_id = request.data['owner_id']
        #   manager_id = request.data['manager_id']
        #   coach_id = request.data['coach_id'] - FOR NOW TEAM CREATOR IS AUTOMATICALLY COACH
        motto = request.data['motto']
        logo = ""
        short_name = request.data['short_name']
        player_ids = []    #   PLAYER IDs

        ##  MODEL VALUES
        
        players = [ Player.objects.get(id=id) for id in player_ids ]
        coach = Coach.objects.get(account=user)

        t = Team.objects.create(name=name, coach=coach, motto=motto, 
            players=players, short_name=short_name)


        status = 200
        message = "Team created successfully"
    
    else:
        status = 415
        message = "Unauthorized to create teams"

    return JsonResponse({
        'status': status,
        'body': {
            'message': message
        }
    })


def request_player(request):
    pass


#   DORMANT FOR NOW
def remove_player(request):
    pass


#   PLAYER ACTIONS
def respond_to_team_request(request):   #   BY PLAYER - ACCEPT OR REJECT TEAM REQUEST

    user = request.user
    team_request = request.data['team_request_id']
