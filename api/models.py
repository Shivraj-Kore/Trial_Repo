from django.db import models
#from datetime import datetime

class Room(models.Model):
    name = models.CharField( max_length=50)