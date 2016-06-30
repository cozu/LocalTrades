from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.utils import timezone
from .models import Item
from django.shortcuts import render, get_object_or_404
from .forms import NewItemForm, UpdateItemForm


def index(request):
    items_list = Item.objects.order_by('-pub_date')
    return render(request, 'items/index.html', {'items_list': items_list})


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'items/detail.html', {'item': item})


def create(request):
    if request.method == 'GET':
        return render(request, 'items/new.html')
    else:
        item_form = NewItemForm(request.POST)
        if item_form.is_valid():
            user = User.objects.first()
            item = Item(name=item_form.cleaned_data['name'], description=item_form.cleaned_data['description'],
                        price=item_form.cleaned_data['price'], photo="", pub_date=timezone.now(), user=user)
            item.save()
            item = Item.objects.get(pk=item.id)
            return render(request, 'items/detail.html', {'item': item})
        else:
            return HttpResponseBadRequest("Invalid data.")


def edit(request, item_id = None):
    if request.method == 'GET':
        item = get_object_or_404(Item, pk=item_id)
        return render (request, 'items/edit.html', {'item': item})
    else:
        item_form = UpdateItemForm(request.POST)
        if item_form.is_valid():
            user = User.objects.first()
            item = get_object_or_404(Item, pk=item_form.cleaned_data['id'])
            item.name = item_form.cleaned_data['name']
            item.description = item_form.cleaned_data['description']
            item.price = item_form.cleaned_data['price']
            item.save()
            return render(request, 'items/detail.html', {'item': item})
        else:
            return HttpResponseBadRequest("Invalid data.")


def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return render(request, 'items/delete.html', {'item': item})
