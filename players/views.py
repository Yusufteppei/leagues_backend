from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Player
from leagues.models import Match, Rating

def user_to_player(user):
    return 1

#   RATING AND VOTING

@api_view(['POST'])
def rate_player(request):
    rating_player = user_to_player(request.user)
    rated_player_id = request.data['rated_player_id']
    match_id = request.data['match_id']
    rating_score = request.data['rating_score']

    rated_player = Player.objects.get(id=rated_player_id)
    match = Match.objects.get(id=match_id)

    Rating.objects.create(rating_player=rating_player,
        rated_player=rated_player_id, match=match_id, rating_score=rating_score)
    
    return JsonResponse({
        'status': 200,
        'message': f'Rating for {rated_player} successful'
    })


@api_view(['POST'])
def vote_award(request):
    competition = ""
    player = ""

    return JsonResponse({
        'status': 200,
        'message': 'Done'
    })