from django.shortcuts import render
from django.http import HttpResponse
def main_page(request):
    date = ['https://i3.mybook.io/p/512x852/book_covers/82/05/8205ea3c-2471-4806-8627-6a711543a776.jpg?v2', 'https://i4.mybook.io/p/512x852/book_covers/7d/76/7d7648dd-b49f-40bb-a1b9-53b933748087.jpe?v2']
    return render(request, 'main_page/main.html')