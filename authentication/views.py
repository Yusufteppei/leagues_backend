from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse


@api_view(['POST'])
def register(request):

    try:
        role_name = request.data['role'] #   ONE ROLE PER USER FOR NOW
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        phone = request.data['phone']
        username = request.data['username']

        role = Role.objects.get(name=role_name)

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


@api_view(['GET'])
def user(request):
    try:
        user = request.user
        body = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
    except:
        status = 401
        body = None
        message = "Unknown User"

    
    return JsonResponse({
        'status': status,
        'body': body,
        'message': message
    })