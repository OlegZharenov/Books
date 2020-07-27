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
descr_prose = 'Современная проза - это проза современных писателей.Современные писатели имеют современное мировоззрение и информативную базу, поэтому их произведения, о чём бы они не писали, относятся к современной прозе.'
descr_hobby = 'Здесь можно найти книги, которые помогут читателю стать лучше в интересующих его отраслях или же открыть для себя новые области деятельности.'
descr_science = 'Научно-популярная литература — литературные произведения о науке, научных достижениях и об учёных, предназначенные для широкого круга читателей.'
descr_psyho = 'Данный раздел позволит читателю разобраться в своих личных проблемах, понять себя, а также приобрести важные жизненные наывки: научиться эффективно коммуницировать, обрести эмоционалльную стабильность и другие. '


for i in result:
    if i[2] not in ListCategory:
        ListCategory.append(i[2])
        ListSlug.append(i[10])

psyho = Category.objects.create(title = ListCategory[0], slug = ListSlug[0], description = descr_psyho, image = 'https://funart.pro/uploads/posts/2020-03/1584638579_11-p-foni-na-temu-psikhologii-41.jpg')
science = Category.objects.create(title = ListCategory[1], slug = ListSlug[1], description = descr_science, image = 'https://avatars.mds.yandex.net/get-pdb/216365/ad387063-cc74-4fc2-828a-8e920cf973cb/s1200?webp=false')
hobby = Category.objects.create(title = ListCategory[2], slug = ListSlug[2], description = descr_hobby, image = 'https://stemeducationguide.com/wp-content/uploads/2019/06/lego-coding-bots-1.jpg')
prose = Category.objects.create(title = ListCategory[3], slug = ListSlug[3], description = descr_prose, image = 'https://cdn.the-village.ru/the-village.ru/post_image-image/y6pQNlZl7d7mMI437X3eqQ-article.jpg')

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
    else:
        post.tag = prose
    post.save()
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
    #post.save()
