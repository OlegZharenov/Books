import os
import django
import sys
import mysql.connector

sys.path.extend(["/Praktika/Murr/Site", "/Praktika/Murr/Site/Site"])

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "settings")
django.setup()

from main.models import Category, Post

tags = Post.objects.filter(genre = 'Современная проза')
print(tags)
