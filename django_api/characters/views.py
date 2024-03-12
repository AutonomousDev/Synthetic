from django.shortcuts import render
from characters.models import Character
from characters.serializers import CharacterSerializer
from rest_framework import viewsets
# Create your views here.


class CharacterViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and creating characters.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
