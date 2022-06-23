from django.shortcuts import render
from django.http import HttpResponse

def index(reqest):
    data = {

        'val': ['wer', 'ret', 'info']
    }


    return render(reqest, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def cont(request):
    return render(request, 'main/contact.html')

def one(request):
    return render(request, 'main/one.html')

def cat(request):
    return render(request, 'main/cat.html')

def hh1(request):
    return render(request, 'main/hh1.html')

def hh2(request):
    return render(request, 'main/hh2.html')

def hh3(request):
    return render(request, 'main/hh3.html')

def hh4(request):
    return render(request, 'main/hh4.html')
