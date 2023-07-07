from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserValidateSerializer, UserCreateSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        if serializer.validated_data.get('password') != password:
            return Response(data={'password': 'password dont match'})
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED, data={'message': 'user created successfully'})


class AuthorizeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message': 'user credentials are wrong'})
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
