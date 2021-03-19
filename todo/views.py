from django.shortcuts import render, redirect, get_object_or_404
from .models import item
from .forms import ItemForm
# Create your views here.


def get_todo_list(request):
    items = item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    form = ItemForm()
    context = {
        "form": form
    }

    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    items = get_object_or_404(item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")
    form = ItemForm(instance=items)
    context = {
        "form": form
    }
    return render(request, "todo/edit_item.html", context)


def toggle_item(request, item_id):
    items = get_object_or_404(item, id=item_id)
    items.done = not items.done
    items.save()
    return redirect("get_todo_list")


def delete_item(request, item_id):
    items = get_object_or_404(item, id=item_id)
    items.delete()
    return redirect("get_todo_list")