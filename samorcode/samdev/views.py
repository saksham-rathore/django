from django.shortcuts import render

# Create your views here.
def samdev(request):
    return render(request, 'samdev/sandev.html')