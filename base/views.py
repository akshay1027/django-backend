from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # context = {'rooms': rooms}
    return render(request, 'base/home.html')


def room(request):
    return HttpResponse("You are in a room")
