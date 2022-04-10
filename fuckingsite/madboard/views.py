from django.http import HttpResponse
from .models import Mb

def index(request):
    s = 'Список обьявлений\r\n\r\n\r\n'
    for mb in Mb.objects.order_by('-published'):
        s += mb.title + '\r\n' + mb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

# Create your views here.
