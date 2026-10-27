from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    #getting data from  post model
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'blog_title' : blog_title, "posts" : posts})


def detail(request, slug):

    # static data
    try :

        #getting data from model by post id
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post doesn't exists")

    # post =next((item for item in posts if item['id'] == post_id), None)
    
    #logger = logging.getLogger("")
    #logger.debug(f"post variable is {post}")
    return render(request, 'blog/detail.html', {'post' : post})

def old_url_redirect(request):
    
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")