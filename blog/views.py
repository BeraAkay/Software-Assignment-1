from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import *
from .models import *
from tags.models import Tag
from .forms import BlogForm

def loggedin(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            form.save_m2m()
    elif request.method == "GET":
            form = BlogForm()

    return render(request,'all.html',{'entries':Blog.objects.filter(owner = request.user.id),
                                      'greet' : "Welcome "+request.user.get_username(),
                                      "tags":Tag.objects.all(),
                                      "form":form})


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

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            form.save_m2m()
    elif request.method == "GET":
            form = BlogForm()


    return render(request,'all.html',{'entries':Blog.objects.filter(owner = request.user.id),
                                      "tags":Tag.objects.all(),
                                      "form":form})

def home(request):
    return render(request,'home.html')