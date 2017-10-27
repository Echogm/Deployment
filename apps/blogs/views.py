# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    return redirect("/register")
def new(request):
    return redirect("/")
def create(request):
    return redirect("/")
def show(request,postnumber):
    response = "This is the post number {}".format(postnumber)
    return HttpResponse(response)
def edit(request,postnumber):
    response = "Edit this is the post number {}".format(postnumber)
    return HttpResponse(response)
def destroy(request,postnumber):
    return redirect("/")
