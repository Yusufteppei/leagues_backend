from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse


@api_view(['POST'])
def register(request):

    try:
        role = request.data['role'] #   ONE ROLE PER USER FOR NOW
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        phone = request.data['phone']
        username = request.data['username']


        u = UserAccount.objects.create(first_name=first_name, last_name=last_name,
                email=email, phone=phone, username=username)
        u.roles.add(role)
        u.save()


        status = 200
        message = "Account created successfully"
    
    except Exception as e:
        raise e
        status = 500
        message = "Account creation failed"

    return JsonResponse({
        'status': status,
        'body': {
            'message': message
        }
    })