# from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    # return HttpResponse("Hello world! i'm Home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("my about page!")
    return render(request, 'about.html')