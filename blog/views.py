# from django.shortcuts import render

# # Create your views here.
# from django.http import HtppResponse

# def blog website(request):
    
#    return HttpResponse(welcome to Barl blogging page)

from django.views.generic import ListView
from .models import Post



class BlogListView(ListView):
  model = Post
  template_name = 'home.html'