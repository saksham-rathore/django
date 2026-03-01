from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hello, world. hey i am sam developer")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("hello, world. hey i am sam developer")

def contact(request):
    return HttpResponse("hello, world. hey i am sam developer")