from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView

# Create your views here.

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetialView(DetailView):
    """Blog Post Detailed View"""

    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","author","body"]