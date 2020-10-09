# from django.shortcuts import render

# # Create your views here.
# from django.http import HtppResponse

# def blog website(request):
    
#    return HttpResponse(welcome to Barl blogging page)

from django.views.generic import ListView ,DetailView
from .models import Post
from django.views.generic.edit import CreateView # new



class BlogListView(ListView):
  model = Post
  template_name = 'home.html'
  
class BlogDetailView(DetailView): # new
  model = Post
  template_name = 'post_detail.html'
  
  
class BlogCreateView(CreateView): # new
 model = Post
 template_name = 'post_new.html'
fields = ['title', 
          'author', 
          'body']