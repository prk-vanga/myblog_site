from django.shortcuts import render

from django.http import HttpResponse
from blog.models import Author, Post, Tag

# Create your views here.

test1 = Post.objects.all()
test2 = Post.objects.all().order_by("-date")

print(f"test1: {type(test1)}")
print(f"test2: {type(test2)}")


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all_posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {
        'post': identified_post
    })
