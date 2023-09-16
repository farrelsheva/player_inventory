from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
# Create your views here.
def show_main(request):
    items = Item.objects.all()
    context = {
        
        'name' : "Farrel Sheva Alkautsar",
        'class' : "PBP A",
        'npm' : "2206030344",
        'items' : items
    }
    return render(request, 'main.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, 'create_item.html', context)
    
    