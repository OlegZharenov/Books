import requests #для отправления запросов
from bs4 import BeautifulSoup

URL = 'https://mybook.ru/catalog/sovremennaya-proza/books/' # ссылка, которую парсим
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
           , 'accept': '*/*'} #Словарь с заголовками, чтобы сервер не посчитал нас за бота. Имитируем работу браузера
host = 'https://mybook.ru'

books = []
links = []
titles = []
authors = []
ratings = []
descriptions = []
year_of_creations = []
size = []

def get_url(url, params = None): #params для передачи номеров страниц
    req = requests.get(url, headers = headers, params = params)
    return req


def get_content(html):
    description_book = ''
    soup = BeautifulSoup(html, 'html.parser') #тип документа с которым работаем. Через soup создаются объекты python с которыми мы можем работать
    divs = soup.find_all('div', class_ = 'ContextBookCardLong__bookTitle')
    for div in divs:
        links.append(host + div.find('a').get('href'))
    for link in links:
        html_book = get_url(link)
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
    print(descriptions)
    print(year_of_creations)
    print(size)



def parse():
    html = get_url(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("ERROR!")

parse()
