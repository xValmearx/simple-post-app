from django.views.generic import ListView, DetailView

# Create your views here.

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetialView(DetailView):
    """Blog Post Detailed View"""

    model = Post
    template_name = "post_detail.html"
