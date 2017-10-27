# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .models import Users, Trip, Travelers
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    # Trip.objects.all().destroy()
    # Travelers.travelersManager.all().delete()
    return render(request, "users/usersIndex.html")
def register(request):
    if request.method == 'POST':
        valid = Users.userManager.register(
            request.POST['name'],
            request.POST['last'],
            request.POST['email'],
            request.POST['password'],
            request.POST['confirmation']
        )
        if valid[0]:
            request.session["email"] = {
            "id": valid[1].id,
            "name": valid[1].name
            }
            return redirect("/travels")
        else:
            for errors in valid[1]:
                messages.add_message(request, messages.ERROR, errors)
            return redirect("/register")
    elif request.method == 'GET':
        return render(request, "users/register.html")
def new_session(request):
    if request.method == 'POST':
        valid = Users.userManager.login(
            request.POST["email"],
            request.POST["password"],
        )
        if valid[0]:
            request.session["email"] = {
                "id": valid[1].id,
                "name": valid[1].name
            }
            return redirect("/travels")
        else:
            for errors in valid[1]:
                messages.add_message(request, messages.ERROR, errors)
        return redirect("/login")
    if request.method == 'GET':
        return render(request, "users/usersLogin.html")

def logout(request):
    request.session.clear()
    return redirect("/register")

def travels(request):
    if 'email' not in request.session:
        return redirect('/login')
    Alltrips = Trip.objects.all()
    usertrips = Travelers.travelersManager.filter(traveler_id = request.session["email"]["id"])
    for trip in usertrips:
        Alltrips = Alltrips.exclude(id = trip.trip.id)
    context = {
        "Alltrips": Alltrips,
        "Trips": usertrips,
    }

    return render(request, "users/travels.html", context)

def create(request):
    Trip.objects.create(
        destination= request.POST["destination"],
        description= request.POST["description"],
        travel_start_date= request.POST["travel_start_date"],
        travel_end_date= request.POST["travel_end_date"],
        creator_id= request.session["email"]["id"]
        )
    return redirect('/travels')


def addplan(request):
    if 'email' not in request.session:
        return redirect('/')
    return render(request, "users/addplan.html")

def users(request):
    return render(request, "users/usersList.html")

def join(request, id):
    if request.method == "POST":
        joins = Travelers.travelersManager.filter(trip_id = id).filter(traveler_id = request.session["email"]["id"])
        if len(joins) == 0:
            Travelers.travelersManager.create(
                traveler_id = request.session["email"]["id"],
                trip_id = id
            )
        return redirect("/travels")

def info(request, id):
    if 'email' not in request.session:
        return redirect('/')
    if request.method == "GET":

        context = {
            "trip": Trip.objects.get(id = id),
            "travelers": Travelers.travelersManager.filter(trip_id = id)
        }
        return render(request, "users/info.html", context)
