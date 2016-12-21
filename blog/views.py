from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import *
from .models import *


def loggedin(request):
    entries = Blog.objects.filter(owner = request.user.id)

    if request.method == "POST":
        new = Blog.objects.create(name=request.POST.get("entr"),
                            description=request.POST.get("desc"),
                            owner = request.user)
        new.tags.add(*request.POST.getlist("tag_names"))
        entries = Blog.objects.filter(owner = request.user.id)


    return render(request,'all.html',{'entries':entries, 'greet' : "Welcome "+request.user.get_username(),"tags":Tag.objects.all()})


def entries(request):
    titles = list()
    for item in Blog.objects.filter(owner = request.user.id):
        titles.append((item.name , item.description))
    titlen = len(titles)
    try:
        x=request.path
        x=x.split("/")
        x=int(x[len(x)-1])
        entry = titles[x]
        return render_to_response('template.html',{'entry':entry[0],'desc':entry[1]})
    except:
        raise Http404('Wrong Page Index, please try between 0 and '+str(titlen-1))

def allentries(request):
    entries = Blog.objects.all()
    if request.user.username :
        entries = Blog.objects.filter(owner = request.user.id)

    if request.method == "POST":
        new = Blog.objects.create(name=request.POST.get("entr"),
                            description=request.POST.get("desc"),
                            owner = request.user)
        new.tags.add(*request.POST.getlist("tag_names"))
        entries = Blog.objects.filter(owner = request.user.id)


    return render(request,'all.html',{'entries':entries,"tags":Tag.objects.all()})

def home(request):
    return render(request,'home.html')