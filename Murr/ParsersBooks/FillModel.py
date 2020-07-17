import os
import django
import sys

sys.path.extend(["/Praktika/Murr/Site", "/Praktika/Murr/Site/Site"])

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "settings")
django.setup()

from main_page.models import Post

from ParsersBooks.ParserProse import books

for i in range(5):
    book = Post.objects.create(title = books[i]['title'], author = books[i]['author'], genre = books[i]['genre'])
    print('Прошло')
