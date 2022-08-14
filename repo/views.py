from http.client import HTTPResponse
from tkinter.tix import Form
from django.shortcuts import render,redirect
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
def all_repo(request):
    posts = Post.objects.all()
    return render(request,'home.html',{"repos":posts})

def single_repo(request,id):
    post = Post.objects.get(id=id)    
    return render (request,"repo_detail.html",{"repo":post})


def home(request):
    return HttpResponse("Hello world")

def edit_repo(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()

    else:
        form = PostForm(instance=post)

    return render(request, 'edit.html', {'form': form})


def new_repo(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = PostForm()

    return render(request,'new.html',{'form':form})



def delete_repo(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/repo")
