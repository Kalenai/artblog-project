# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now
import datetime

def home(request):
    today = datetime.date.today()
    return render(request, "artblog/index.html", {'today': today, 'now': now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def about(request):
    return render(request, "artblog/templates/flatpages/about.html")

def contact(request):
    return render(request, "artblog/templates/flatpages/contact.html")
