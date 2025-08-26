from django.shortcuts import render


import os
from django.conf import settings


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


def lista_pdfs(request):
 
    pdf_folder = os.path.join(settings.MEDIA_ROOT, "intro_u1")
    pdf_files = os.listdir(pdf_folder) if os.path.exists(pdf_folder) else []
    pdf_urls = [
        {"name": f, "url": settings.MEDIA_URL + "intro_u1/" + f}
        for f in pdf_files if f.endswith(".pdf")
    ]

    return render(request, "blog/pdfs_u1_intro.html", {"pdfs": pdf_urls})
