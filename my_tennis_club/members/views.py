from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
# Note: views are Python functions that takes http requests and returns http response, like HTML documents.
def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "my_members": my_members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_member = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "my_members": my_member,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    members = Member.objects.all()
    template = loader.get_template("template.html")
    context = {
        'greeting':2,
        'members': members,
        'prices' : [1,2,3,3,4,4,5,6,6,7,7,7],
        'fruits' : ['apple', 'mango', 'pineapple', "grapes",'banana', 'mango'],
        'vegetables': ['onion', 'tomato', 'carrot'],
        'name' : 'shinchan\nnohara',
        'my_dict': [
            {'name': 'shinchan', 'age': 5},
            {'name': 'naruto', 'age': 22},
            {'name': 'tom', 'age': 60}
        ],
        'value':40,
        'day': 'Monday',
        'cars': [
        {
            'brand': 'Ford',
            'model': 'Mustang',
            'year': '1964',
        },
        {
            'brand': 'Ford',
            'model': 'Bronco',
            'year': '1970',
        },
        {
            'brand': 'Ford',
            'model': 'Sierra',
            'year': '1981',
        },
        {
            'brand': 'Volvo',
            'model': 'XC90',
            'year': '2016',
        },
        {
            'brand': 'Volvo',
            'model': 'P1800',
            'year': '1964',
        }],
        'x' : [1, 2, 3],
        'y' : [1, 2, 3],
    }
    

    return HttpResponse(template.render(context, request))
    # return HttpResponse(template.render())
