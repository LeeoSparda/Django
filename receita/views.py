from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html', context={
        'name':'Leonardo Borges',
    })

#HTTP REQUEST
def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse('SOBRE')