# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    return render(request, "surveys/surveysIndex.html")
def new(request):
    return render(request, "surveys/surveysNew.html")