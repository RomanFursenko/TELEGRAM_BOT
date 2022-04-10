from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('В ПОСЛЕДНИЙ РАЗ ПОВТОРЮ: Русскиий военный корабыль - ИДИ НА ХУЙ!!!')
