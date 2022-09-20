from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import interface
##########################################

def search_ID(request):
  template = loader.get_template('search_ID.html')
  return HttpResponse(template.render({}, request))
##########################################

def searchidindex(request):
  mymembers = interface.objects.all().values()
  template = loader.get_template('ID_index.html')
  context = {
    'interfaces': mymembers,
  }
  return HttpResponse(template.render(context, request))
##########################################

def search_int(request):
  mymembers = interface.objects.all().values()
  template = loader.get_template('search_int.html')# in template folder
  context = {
    'interfaces': mymembers,
  }
  return  HttpResponse(template.render(context, request))
##########################################

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render({}, request)) 










##########################################

def database_index(request):
  mymembers = interface.objects.all().values()
  template = loader.get_template('myint/index.html')# in template/myint/ folder
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))
##########################################
def int_index(request):
  mymembers = interface.objects.all().values()
  template = loader.get_template('int_index.html')# in template folder
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))
##########################################
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
##########################################
def addrecord(request):
  r = request.POST['router']
  x = request.POST['name']
  y = request.POST['des']
  w = request.POST['id']
  z = request.POST['ip']
  t = request.POST['profile']
  s = request.POST['type']

  member = interface(Router_Name= r, int_Name= x, Description= y,
                  int_ID= w, IP= z, Profile= t, Int_type= s)
  member.save()
  return HttpResponseRedirect(reverse('index'))

###########################################
def testing(request):
  mymembers = interface.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))
###########################################



