from django.http import HttpResponse
from .models import Item
from django.template import loader


def index(request):
    items_list = Item.objects.order_by('-pub_date')
    template = loader.get_template('items/index.html')
    return HttpResponse(template.render({ 'items_list': items_list }, request))