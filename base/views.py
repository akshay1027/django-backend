from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("you are in home page")


def room(request):
    return HttpResponse("You are in a room")
