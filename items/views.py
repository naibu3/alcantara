from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import CreateItemForm, UpdateItemForm

def index(request):

    context={}
    
    return render(request, 'items-index.html', context)

#CREATE ITEM______________________________________________________
def create_item_form(request):

    context={'create_item_form': CreateItemForm()}

    return render(request, 'items-create-form.html', context)

def create_item(request):

    if request.method != 'POST':
        status="Method not allowed"
        context={'status':status}
        return render(request, 'items-error.html', context)

    form = CreateItemForm(request.POST)
    if form.is_valid():
        
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        uds = form.cleaned_data['uds']
        place = form.cleaned_data['place']

        if Item.objects.filter(name=name).exists():
            status="Object ("+name+") already exists"
            context={'status':status}
            return render(request, 'items-error.html', context)
        
        item = Item(name=name, comment=comment, uds=uds, place=place)
        item.save()

        status="Item ("+item.name+", "+item.comment+", "+str(item.uds)+", "+item.place+") creado con exito"
        context={'status':status}
        return render(request, 'items-success.html', context)

    return render(request, 'items-error.html', context)

#LIST ITEMS_______________________________________________________
def list_items(request):

    if request.method != 'GET':
        status="Method not allowed"
        context={'status':status}
        return render(request, 'items-error.html', context)

    items = Item.objects.all()
    
    context={'items':items}

    return render(request, 'items-list.html', context)

#SEARCH ITEMS_____________________________________________________
def search_items(request):

    query = request.GET.get('query', '').strip()
    items=None
    
    if query:
        items = Item.objects.filter(name__icontains=query)

    context = {'items': items, 'query': query}

    return render(request, 'items-search.html', context)

#UPDATE ITEM______________________________________________________
def update_item_form(request, name):

    if request.method != 'GET':
        status="Method not allowed"
        context={'status':status}
        return render(request, 'items-error.html', context)

    item = get_object_or_404(Item, name=name)

    context={'update_item_form': UpdateItemForm(initial={'name':name,
                                                         'comment':item.comment,
                                                         'uds':item.uds,
                                                         'place':item.place})}

    return render(request, 'items-update-form.html', context)

def update_item(request):

    if request.method != 'POST':
        status="Method not allowed"
        context={'status':status}
        return render(request, 'items-error.html', context)

    form = UpdateItemForm(request.POST)
    if form.is_valid():
        
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        uds = form.cleaned_data['uds']
        place = form.cleaned_data['place']

        if not Item.objects.filter(name=name).exists():
            status="Object ("+name+") does not exists"
            context={'status':status}
            return render(request, 'items-error.html', context)
        
        item = Item(name=name, comment=comment, uds=uds, place=place)
        item.save()

        status="Item ("+item.name+", "+item.comment+", "+str(item.uds)+", "+item.place+") actualizado con exito"
        context={'status':status}
        return render(request, 'items-success.html', context)

    return render(request, 'items-error.html', context)

#DELETE ITEM______________________________________________________
def delete_item(request):

    if request.method != 'POST':
        status="Method not allowed"
        context={'status':status}
        return render(request, 'items-error.html', context)


    name=request.POST['name']

    item = Item.objects.get(name=name)
    item.delete()
    
    status="Item (" + name + ") borrado con exito"
    context={'status':status}
    return render(request, 'items-success.html', context)

def custom_page_not_found(request, exception):
    status="404 Not found"
    context={'status':status}
    return render(request, 'items-error.html', context, status=404)