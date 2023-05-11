from django.shortcuts import render 
from rest_framework.generics import ListAPIView , RetrieveAPIView ,DestroyAPIView , UpdateAPIView , CreateAPIView
from . models import Room

from . serializers import RoomSerializer


class RoomNamesList(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomNamesCreate(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomNamesDestroy(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomNamesUpdate(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomNamesRetrieve(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer