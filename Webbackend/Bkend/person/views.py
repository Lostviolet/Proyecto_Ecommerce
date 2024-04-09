from django.shortcuts import render
from .models import person_connectiondb
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Home Page</h1>')

def add_person(request):
    records={
        "first_name":"Fabiola",
        "last_name":"Torres",
        "email":"marie8_91@hotmmail.com",
        "password":"1234",
        "confirm_password":"1234" 
    }
    person_connectiondb.insert_one(records)
    return HttpResponse("Add New Person")

def get_all_person(request):
    persons=person_connectiondb.find()
    return HttpResponse(persons)
