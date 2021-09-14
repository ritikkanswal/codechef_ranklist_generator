from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=50)
    rating = models.IntegerField()
    highest_rating=models.IntegerField()
    global_rank=models.IntegerField()
    country_rank=models.IntegerField()



