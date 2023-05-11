from django.contrib import admin
from . models import Room


admin.site.register(Room)

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name']