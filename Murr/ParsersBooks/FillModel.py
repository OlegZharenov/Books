import os
import django
import sys
import mysql.connector

sys.path.extend(["/Praktika/Murr/Site", "/Praktika/Murr/Site/Site"])

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "settings")
django.setup()

from main.models import *
ListCategory = []
ListSlug = []
connection = mysql.connector.connect(host = 'localhost',
                             user = 'root',
                             password = '89379608523QqQ',
                             database = 'books')

cursor = connection.cursor()
cursor.execute("SELECT * FROM books_info")
result = cursor.fetchall()
#Создаем категории


for i in result:
    if i[2] not in ListCategory:
        ListCategory.append(i[2])
        ListSlug.append(i[10])

psyho = Category.objects.create(title = ListCategory[0], slug = ListSlug[0])
science = Category.objects.create(title = ListCategory[1], slug = ListSlug[1])
hobby = Category.objects.create(title = ListCategory[2], slug = ListSlug[2])
prose = Category.objects.create(title = ListCategory[3], slug = ListSlug[3])

#Заполняем посты
for i in range(len(result)):
    post = Post()
    post.title = result[i][0]
    post.author = result[i][1]
    post.genre = result[i][2]
    post.link = result[i][7]
    post.slug = result[i][9]
    if result[i][2] == ListCategory[0]:
         post.tag = psyho
    elif result[i][2] == ListCategory[1]:
         post.tag = science
    elif result[i][2] == ListCategory[2]:
        post.tag = hobby
    # else:
    #     post.tag = prose
    # post.save()
    # book = Book()
    # book.title = result[i][0]
    # book.author = result[i][1]
    # book.genre = result[i][2]
    # book.rating = result[i][3]
    # book.year = result[i][4]
    # book.size = result[i][5]
    # book.description = result[i][6]
    # book.link = result[i][7]
    # book.slug = result[i][9]
    # if result[i][2] == ListCategory[0]:
    #      post.tag = psyho
    # elif result[i][2] == ListCategory[1]:
    #      post.tag = science
    # elif result[i][2] == ListCategory[2]:
    #     post.tag = hobby
    # else:
    #     post.tag = prose
    book.save()
