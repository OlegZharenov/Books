from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=40, db_index=True)
    description = models.TextField(db_index=True, blank=True)
    image = models.CharField(max_length=300, blank=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)


    def __str__(self):
        return '{}'.format(self.title)


class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=50, db_index=True)
    genre = models.CharField(max_length=40, db_index=True)
    rating = models.CharField(max_length=50, db_index=True)
    year = models.CharField(max_length=50, db_index=True)
    size = models.CharField(max_length=50, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    image = models.ImageField(upload_to='book_image')
    link = models.CharField(max_length=150, default = 'image', db_index=True)


    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=50, db_index=True)
    genre = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='book_image')
    link = models.CharField(max_length=150, default = 'image', db_index=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='Tag')


    def __str__(self):
        return '{}'.format(self.title)