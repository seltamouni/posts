from django.shortcuts import render
from .models import Post

# Create your views here.
def all_repo(request):
    post = Post.objects.all()
    return render(request,'home.html',{"bolg":post})

def single_repo    