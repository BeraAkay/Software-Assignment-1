from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import *
from .models import *

def loggedin(request):
    entries = Blog.objects.all()
    entry = list()
    for item in entries:
        entry.append((item.name,item.description))

    if request.method == "POST":
        Blog.objects.create(name=request.POST.get("entr"),
                            description=request.POST.get("desc"))
        entries = Blog.objects.all()
        entry = list()
        for item in entries:
            entry.append((item.name, item.description))

    return render(request,'all.html',{'entries':entry, 'greet' : "Welcome "+request.user.get_username()})


def entries(request):
    titles = list()
    for item in Blog.objects.all():
        titles.append((item.name , item.description))
    try:
        x=request.path
        x=x.split("/")
        x=int(x[len(x)-1])
        entry = titles[x]
        return render_to_response('template.html',{'entry':entry[0],'desc':entry[1]})
    except:
        raise Http404('Wrong Page Index, please try between 0 and '+str(titleamount-1))

def allentries(request):
    entries = Blog.objects.all()
    entry = list()
    for item in entries:
        entry.append((item.name,item.description))
    if request.method == "POST":
        Blog.objects.create(name=request.POST.get("entr"),
                            description=request.POST.get("desc"))
        entries = Blog.objects.all()
        entry = list()
        for item in entries:
            entry.append((item.name, item.description))

    return render(request,'all.html',{'entries':entry})

def home(request):
    return render(request,'home.html')