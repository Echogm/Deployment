# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
import bcrypt
# Create your models here.
# try:
#     validate_email(email.POST["email"])
#     valid_email = True
# except validate_email,ValidationError:
#     valid_email = False
class UserManager(models.Manager):
    def register(self, name, last, email, password, confirmation):

        errors = []

        if len(name) < 3:
            errors.append("Name most be 2 characters or longer!")
        if len(last) < 3:
            errors.append("Last name must be 2 characters or longer!")
        if len(Users.userManager.filter(email=email)) > 0:
            errors.append("This email is already taken.")
        if len(password) < 8:
            errors.append("Password most be 8 characters or longer!")
        if not password == confirmation:
            errors.append("Passwords must match.")
        if len(errors) > 0:
            return(False, errors)
        else:
            passwordHashed =bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = Users.userManager.create(name=name, lastName=last, email=email, passwordHashed=passwordHashed)
            return (True, user)
    def login(self, email, password):
        errors = []

        if len(email) < 2:
            errors.append("Email must be 2 characters or longer!")
        if len(password) < 8:
            errors.append("Password must be 8 characters or longer!")

        email = Users.userManager.filter(email=email)

        if len(email) == 0:
            errors.append("Email not found!")

        if len(errors) > 0:
            return (False, errors)

        else:
            if bcrypt.checkpw(password.encode(), email[0].passwordHashed.encode()):
                return (True, email[0])
            else:
                return (False, ["Incorrect Password!"])


class Users(models.Model):
    name = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    passwordHashed = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    travel_start_date = models.CharField(max_length = 255)
    travel_end_date = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(Users, related_name = "travels")
    def __repr__(self):
        return "<Trip: {} {} {} {}".format(
            self.destination,
            self.description,
            self.travel_start_date,
            self.travel_end_date
    )

class TravelersManager(models.Manager):
    def travelers(self, traveler, trip):
        if Travelers.travelersManager.filter(traveler_id = traveler) == traveler_id:
            print "This user is already in this trip"
            return False
        if len(Travelers.travelersManager.filter(traveler_id = traveler).filter(trip_id = trip)) == 0:
            Travelers.travelersManager.create( traveler_id=traveler, trip_id = trip)
            return True
        else:
            return False
    def getbyid(self, id):
        return self.get(id=id)
class Travelers(models.Model):
    traveler = models.ForeignKey(Users, related_name="traveler")
    trip = models.ForeignKey(Trip, related_name="travel")

    travelersManager = TravelersManager()
