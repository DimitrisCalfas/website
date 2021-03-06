# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Album
from django.shortcuts import render

# Create your views here.

def index(request):

    all_albums = Album.objects.all()
    context = {"all_albums" : all_albums}
    return render(request,'music/index.html',context)

def detail(request,album_id):
    try:
        album=Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist!")
    return render(request,'music/detail.html',{'album': album})




