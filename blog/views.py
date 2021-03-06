from django.shortcuts import render

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on') #we have arranged all the posts by their creation date. + he ( – ) sign before the created_on signifies the latest post would be at the top and so on.
    template_name = 'index.html' 

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def index(request):
    return render(request, "blog/homepage.html")