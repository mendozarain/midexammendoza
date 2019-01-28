from django.db import models
from django.utils import timezone


# Create your models here.

class Position(models.Model):
    name= models.CharField(max_length=100)
    description= models.CharField(max_length=250)

    def __str__(self):
        return self.name
        
class Candidate(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    position= models.ForeignKey(Position, on_delete=models.CASCADE)
    birthdate = models.DateTimeField('date of birth')
    platform =models.TextField()

    def __str__(self):
        return self.firstname



class Vote(models.Model):
    candidate= models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vote_datetime=  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.candidate
