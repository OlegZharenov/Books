from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=200, db_index=True)
    Author = models.CharField(max_length=50, db_index=True)
    Genre = models.CharField(max_length=40, db_index=True)
    Rating = models.CharField(max_length=50, db_index=True)
    Year = models.CharField(max_length=50, db_index=True)
    Size = models.CharField(max_length=50, db_index=True)
    Description = models.TextField(blank=True, db_index=True)
    #Image = models.CharFieldField()
# Create your models here.
