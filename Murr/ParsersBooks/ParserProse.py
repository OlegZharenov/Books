import requests #для отправления запросов
from bs4 import BeautifulSoup
import os


URL_CAT = ['https://mybook.ru/catalog/sovremennaya-proza/books/', 'https://mybook.ru/catalog/nauka-obrazovanie/books/', 'https://mybook.ru/catalog/knigi-po-psihologii/books/', 'https://mybook.ru/catalog/hobbi-dosug/books/'] # ссылка, которую парсим
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
           , 'accept': '*/*'} #Словарь с заголовками, чтобы сервер не посчитал нас за бота. Имитируем работу браузера
host = 'https://mybook.ru'
count = 1
category = ''


URLS = []
books = []
links_page = []
links_image = []


def pages_with_books(URL):
    html = get_url(URL)
    url_page = URL + '?page='
    count_page = get_pages_count(html.text)
    for number in range(1, count_page+1):
        URLS.append(url_page+str(number))

def get_slug(string):
    res = ''
    New_string = string.lower()
    New_List = New_string.split()
    for i in New_List:
        if '.' in i or ',' in i:
            i = i[:-1]
        res = res + i + '-'
    result = res[:-1]
    return result


def get_url(url, params = None): #params для передачи номеров страниц
    req = requests.get(url, headers = headers, params = params)
    return req


def get_image_link(html_book):#получаем ссылки на изображения
    soup_image = BeautifulSoup(html_book.text, 'html.parser')
    link_image = soup_image.find_all('img', class_ = 'BookCoverImage__coverImage BookCoverImage__coverImageText')
    for image in link_image:
        links_image.append(image['src'])
    return links_image[-1]


def get_url_image(url_img):#Функция, для того, чтобы отправить корректный запрос для картинки
    req_img = requests.get(url_img, stream = True)
    return req_img


def get_name_image(count):#Собираем имя для очередной обложки
    folder = 'Books_Covers'
    if not os.path.exists(folder):
        os.mkdir(folder)
    path = os.path.abspath(folder)
    return path + '/' + str(count)


def get_image(request_object, count):#скачиваем одну обложку
    name_img = get_name_image(count)
    with open (name_img+'.jpg', 'bw') as file:
        for chunk in request_object.iter_content(8192):
            file.write(chunk)


def get_image_content(count):#Итерируясь по ссылкам скачиваем обложки
    for link_img in links_image:
        get_image(get_url_image(link_img), count)
        count = count + 1


def get_link_pages_book(html):#собираем ссылки со страниц, на которых подробная информация о книгах и парсим контент
    soup = BeautifulSoup(html, 'html.parser') #тип документа с которым работаем. Через soup создаются объекты python с которыми мы можем работать
    category = soup.find('div', class_ = 'sectionHeader')
    category = category.text.split('«')[-1][0:-1]
    divs = soup.find_all('div', class_ = 'ContextBookCardLong__bookTitle')
    for div in divs:
        links_page.append(host + div.find('a').get('href'))
    get_content(category)
    get_image_content(count)
    links_page.clear()


def get_content(category):#собираем ТЕКСТОВУЮ информацию со страницы, где подробная информация о книгах
    for link in links_page:
        description_book = ''
        size = ''
        year_of_creations = ''
        html_book = get_url(link)
        image = get_image_link(html_book)#Собираем ссылки обложек
        soup_book = BeautifulSoup(html_book.text, 'html.parser')
        titles_book = soup_book.find('h1', class_='BookPageHeaderContent__coverTitle').text
        slug = get_slug(titles_book)
        author_book = soup_book.find('a', class_='BookAuthor__authorName').text
        rating = 'Рейтинг: ' + soup_book.find('span', class_='BookPageHeaderContent__bookRatingCount').text
        information_book = soup_book.find('div', class_ = 'BookDetailAnnotation__descriptionWrapper')
        for description in information_book.find_all('p'):
            if 'MyBook.ru' in description.text or 'Год издания' in description.text or 'ISBN' in description.text or 'Дата поступления' in description.text or 'Купить книгу' in description.text:
                continue
            if 'Дата написания:' in description.text:
                year_of_creations = description.text
                continue
            if 'Объем:' in description.text:
                size = description.text
                continue
            description_book = description_book + description.text + '\n'
        if size == '':
            size = 'Объем книги неизвестен.'
        if year_of_creations == '':
            year_of_creations = 'Год написания книги неизвестен.'
        if description_book == '':
            description_book = 'Описание отсутствует.'
        books.append({'title': titles_book, 'author' : author_book, 'genre': category, 'rating': rating,
                      'year': year_of_creations, 'size': size, 'description': description_book, 'img': image, 'link': link, 'slug':slug})


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser') #тип документа с которым работаем. Через soup создаются объекты python с которыми мы можем работать
    pagenation = soup.find_all('span', class_ = 'PageButton__button')
    max_count = int(pagenation[-1].get_text())
    if max_count>1:
        return 1
    else:
        return max_count


def parse():
    for URL in URL_CAT:
        html = get_url(URL)
        if html.status_code == 200:
            count_page = get_pages_count(html.text)
            pages_with_books(URL)
            for url in URLS:
                html = get_url(url)
                get_link_pages_book(html.text)
        else:
            print("ERROR!")
        URLS.clear()
    print(books)


parse()