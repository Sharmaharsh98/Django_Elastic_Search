from django.shortcuts import render
from .documents import AlphaDocs

# Create your views here.
def search(request):
    a = request.GET.get('a')

    if a:
        alphabets = AlphaDocs.search().query('match', alphabet = a)
    else:
        alphabets = ''
    return render(request, 'index.html', context={'alphabets': alphabets})
