from django.http import HttpResponse
from django.template import loader

from .models import Mb

def index(request):
    template = loader.get_template('madboard/index.html')
    mbs = Mb.objects.order_by('-published')
    context = {'mbs':mbs}
    return HttpResponse(template.render(context, request))
