from django.db import models


class Movies(models.Model):

    def __str__(self) :
        return self.name
    
    name= models.CharField(max_length=200)
    rating=models.FloatField()
