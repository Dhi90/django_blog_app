from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import blog,AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
# static demo data
# posts=[
#         {'id':1,'title':'post 1','content':'content of the post 1'},
#         {'id':2,'title':'post 2','content':'content of the post 2'},
#         {'id':3,'title':'post 3','content':'content of the post 3'},
#         {'id':4,'title':'post 4','content':'content of the post 4'},
#     ]


def index(request):
    blog_tile = "Latest Blogs"
    # getting data from blog model
    all_posts = blog.objects.all()
    
    #paginate all posts
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "index.html", {"blog_tile": blog_tile, "page_obj":page_obj})


def detail(request, slug):
    # static metod for blog
    # post=next((item for item in posts if item['id']==int(post_id)),None)
    # getting data from blog by post_id
    try:
        post = blog.objects.get(slug=slug)
        related_posts = blog.objects.filter(category=post.category).exclude(pk=post.id)
        
    except blog.DoesNotExist:
        raise Http404("post page doen't exist")

    # logger=logging.getLogger("Testing")
    # logger.debug(f"post variable is {post}")


    return render(request, "detail.html", {"post": post,"related_posts": related_posts})


def old_url_redirecting(request):
    return redirect(reverse("blog:new_page_url"))


def new_url_view(request):
    return HttpResponse("this is the new url")

def contact_view(request):
    if request.method == "POST":  # Fixing the method check
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')  
        logger = logging.getLogger("Testing")
        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            #send email or save in database
            success_message = 'Your Email has been sent!'
            return render(request,'contact.html', {'form':form,'success_message':success_message}) 
        else:
            logger.debug(f"Form is not valid ")
        return render(request, "contact.html",{'form':form, 'name': name, 'email':email, 'message': message})
  
    return render(request, "contact.html")

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'about.html',{'about_content':about_content})