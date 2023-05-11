from django.urls import path
from api import views

urlpatterns = [
    path('room/' , views.RoomNamesList.as_view() ),
    path('room/create/' , views.RoomNamesCreate.as_view() ),
    path('room/destroy/' , views.RoomNamesDestroy.as_view() ),
    path('room/<pk>/update/' , views.RoomNamesUpdate.as_view() ),
]
