from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    #getting data from  post model
    all_posts = Post.objects.all()

    #paginate
    paginator= Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'blog_title' : blog_title, "page_obj": page_obj})


def detail(request, slug):

    # static data
    try :

        #getting data from model by post id
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post doesn't exists")

    # post =next((item for item in posts if item['id'] == post_id), None)
    
    #logger = logging.getLogger("")
    #logger.debug(f"post variable is {post}")
    return render(request, 'blog/detail.html', {'post' : post, 'related_posts': related_posts})

def old_url_redirect(request):
    
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact_view(request):
    logger = logging.getLogger("TESTING")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if form.is_valid():
            logger.debug(f"post variable is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']} ")
            success_message = 'Your Email has been sent!'
            return render(request, 'blog/contact.html', {'form': form,'success_message': success_message})

        else :
            logger.debug('Form validation failure')
        return render(request, 'blog/contact.html', {'form': form, 'name' :name, 'email':email,'message': message})
    return render(request, 'blog/contact.html')
