from django.urls import path

from .views import BlogListView, BlogDetialView

urlpatterns = [
    path("post/<int:pk>/", BlogDetialView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
]
