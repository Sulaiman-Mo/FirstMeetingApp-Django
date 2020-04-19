from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meeting.models import Metting




def welcome(request):
    return render(request, "wibsite/welcome.html",
    {"meetings": Metting.objects.all()})


def date(request):
    return HttpResponse("This page was served at"+ " " + str(datetime.now()))


def about(request):
    return HttpResponse("My name is sulaiman i so exited to learn more about django")