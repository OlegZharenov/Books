import requests #для отправления запросов
from bs4 import BeautifulSoup
import os


URL = 'https://mybook.ru/catalog/sovremennaya-proza/books/' # ссылка, которую парсим
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
           , 'accept': '*/*'} #Словарь с заголовками, чтобы сервер не посчитал нас за бота. Имитируем работу браузера
host = 'https://mybook.ru'
count = 0


books = []
links_page = []
links_image = []
titles = []
authors = []
ratings = []
descriptions = []
year_of_creations = []
size = []


def get_url(url, params = None): #params для передачи номеров страниц
    req = requests.get(url, headers = headers, params = params)
    return req


def get_image_link(html_book):#получаем ссылки на изображения
    soup_image = BeautifulSoup(html_book.text, 'html.parser')
    link_image = soup_image.find_all('img', class_ = 'BookCoverImage__coverImage BookCoverImage__coverImageText')
    for l_i in link_image:
        links_image.append(l_i['src'])


def get_url_image(url_img):#Функция, для того, чтобы отправить корректный запрос длля картинки
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
    divs = soup.find_all('div', class_ = 'ContextBookCardLong__bookTitle')
    for div in divs:
        links_page.append(host + div.find('a').get('href'))
    get_content()
    get_image_content(count)


def get_content():#собираем ТЕКСТОВУЮ информацию со страницы, где подробная информация о книгах
    description_book = ''
    for link in links_page:
        html_book = get_url(link)
        get_image_link(html_book)#Собираем ссылки обложек
        soup_book = BeautifulSoup(html_book.text, 'html.parser')
        titles_book = soup_book.find('h1', class_='BookPageHeaderContent__coverTitle').text
        author_book = soup_book.find('a', class_='BookAuthor__authorName').text
        rating = soup_book.find('span', class_='BookPageHeaderContent__bookRatingCount').text
        titles.append(titles_book)
        authors.append(author_book)
        ratings.append('Рейтинг: '+ rating)
        information_book = soup_book.find('div', class_ = 'BookDetailAnnotation__descriptionWrapper')
        for description in information_book.find_all('p'):
            if 'MyBook.ru' in description.text or 'Год издания' in description.text or 'ISBN' in description.text or 'Дата поступления' in description.text or 'Купить книгу' in description.text:
                continue
            if 'Дата написания:' in description.text:
                year_of_creations.append(description.text)
                continue
            if 'Объем:' in description.text:
                size.append(description.text)
                continue
            description_book = description_book + description.text + '\n'
        descriptions.append(description_book)
    #print(descriptions)
    #print(year_of_creations)
    #print(size)
    #print(links_page.text)
    #print(links_image)


def parse():
    html = get_url(URL)
    if html.status_code == 200:
        get_link_pages_book(html.text)
    else:
        print("ERROR!")

parse()
