from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello mundo</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
    #return HttpResponse("<h1>Contact Page</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
    	"title": "this is about us",
    	"this_is_true": True,
    	"my_number": 1234567,
    	"my_list": [453, 20, 2456, 9876, 'abc'],
    	"athlete_list": ['mark', 'laura', 'ingrid', 'kira', 'jennifer', 'bonham-carter'],
    	"athlete_in_locker_room_list": ['norman', 'joe', 'ali', 'ramon'],
    	"my_html": "<h1>Hello marcelo mate</h1>"

    }
    return render(request, "about.html", my_context)
    #return HttpResponse("<h1>About Page</h1>")

def my_page_view(request, *args, **kwargs):
    return render(request, "myview.html", {})
