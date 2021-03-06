from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts':posts})


def post_deatils(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_details.html', {'post':post})