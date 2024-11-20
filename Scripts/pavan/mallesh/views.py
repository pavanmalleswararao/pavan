from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Mallesh

def mallesh(request):
    mymallesh=Mallesh.objects.all().values()
    template=loader.get_template('allmallesh.html')
    context={
        'mymallesh':mymallesh,
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    mymallesh=Mallesh.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mymallesh':mymallesh,
    }
    return HttpResponse(template.render(context,request)) 
    
def  main(request):
     
    template=loader.get_template('main.html')
    return HttpResponse(template.render()) 
    