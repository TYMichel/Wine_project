from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
app_name = 'my_app'

def welcome_view(request,**kwargs):
     if kwargs: 
          greetings = f"<html><h1>Welcome to my Website {str(kwargs['prenom']).title()} ! </h1></html>"
          return HttpResponse(content=greetings)
     else : 
          return render(request,"index.html")

def acceuil_view(request):
     liens = {
          "lien_bobo" : "bobo/",
          "lien_erland" : "erland/",
          "lien_luther" : "luther/"
     }
     return render(request,"acceuil.html",liens)