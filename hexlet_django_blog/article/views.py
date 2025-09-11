from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Статьи'
    }
    return render(request, 'articles/index.html', context)