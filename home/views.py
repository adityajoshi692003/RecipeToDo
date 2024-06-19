from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hey!! I'm a Django server</h1")

    data=[{"Name":'Aman Kumar', "Age":20},
    {"Name":'Ajay', "Age":24},
    {"Name":'Ram', "Age":16},
    {"Name":'Rahul', "Age":22}]

    for d in data:
        print(d)

    return render(request, "home/index.html", context={'data':data}) # Linking Django server and html
def about(request):
   # return  HttpResponse("<h1>Hey!! It's a success</h1") 
    return render(request, "home/about.html") # Linking Django server and html
def contact(request):
   # return  HttpResponse("<h1>Hey!! It's a success</h1") 
    return render(request, "home/contact.html")



#def success_page(request):
 #   return  HttpResponse("<h1>Hey!! It's a success</h1")