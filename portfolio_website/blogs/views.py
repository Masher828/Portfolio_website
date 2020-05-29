from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def allblogs(request):
    blog = Blog.objects
    return render (request, 'blogs/allblogs.html',{'blogs':blog})

def blog_details(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blogs/blog_details.html',{'blog':blog})
