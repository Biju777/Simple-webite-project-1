from django.shortcuts import render
from tech.models import Blog
# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    return render(request, "blogs/blog.html", {
        "blogs":blogs
    })


def post(request, slug):
    post = Blog.objects.filter(slug=slug).first()
    return render(request, 'blogs/post.html', {
        "post":post
    })
