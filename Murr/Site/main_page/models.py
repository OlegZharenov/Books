from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=50, db_index=True)
    genre = models.CharField(max_length=40, db_index=True)
    rating = models.CharField(max_length=50, db_index=True)
    year = models.CharField(max_length=50, db_index=True)
    size = models.CharField(max_length=50, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    image = models.ImageField(upload_to='book_image')

    def __str__(self):
        return f'{self.title}'
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=50, db_index=True)
    genre = models.CharField(max_length=40, db_index=True)
    image = models.ImageField(upload_to='book_image')

    def __str__(self):
        return '{}'.format(self.title)