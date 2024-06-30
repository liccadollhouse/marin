from django.db import models


# Create your models here.

VALID_DIVISIONS = [
    ("youth","Youth"),
    ("novice","Novice"),
    ("journeyman","Journeyman"),
    ("master","Master"),
    ("skit","Skit"),
    ("exhibition","Strut Your Stuff"), # AnimeFest/GameFest has an exhibition division called "Strut Your Stuff".
]


class Division(models.Model):
    division_name = models.CharField(max_length=50,choices=VALID_DIVISIONS,default="novice")

class ContestEntry(models.Model):
    cosplay_name = models.CharField(max_length=50)
    character = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    judging_time = models.CharField(max_length=50)  
    division = models.ForeignKey(Division,on_delete=models.CASCADE)
    
    

