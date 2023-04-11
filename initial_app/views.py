from django.shortcuts import render
from .models import Initial_app

def index(request):
    todo_items = Initial_app.objects.order_by("id")
    context = {'todo_items': todo_items}
    return render(request, 'initial_app/index.html', context)
