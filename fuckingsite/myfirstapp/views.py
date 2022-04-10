from django.http import HttpResponse
from django.template import loader

from .models import Fa

def index(request):
    template = loader.get_template('myfirstapp/index.html')
    mfs = Mb.objects.order_by('-published')
    context = {'mfs':mfs}
    return HttpResponse(template.render(context, request))
