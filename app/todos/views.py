from django.shortcuts import redirect, render

from .models import Item, List


# Create your views here.
def home_page(request):
    return render(request, 'todos/home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/todos/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/todos/{list_.id}/')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'todos/list.html', {'list': list_})
