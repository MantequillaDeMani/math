from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def pagina_css(request):
    return render(request, 'blog/index.html')
def numeros(request):
    return render(request, 'blog/numeros.html')
def intro(request):
    return render(request, 'blog/tr_u1.html')

def ejercicios(request):
    return render(request, 'blog/ejercicios_u1.html')

def ejercicios2_u1(request):
    return render(request, 'blog/ejercicios2_u1.html')

def numeros2(request):
    return render(request, 'blog/numeros2.html')