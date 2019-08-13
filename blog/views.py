
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.files.storage import FileSystemStorage

def createblog(request):
    if request.method == 'POST':


        print(request.POST)
        title = request.POST['title']
        blog_photo = request.FILES['image']
        textbody = request.POST['textbody']

        b = Blog()
        b.title = title
        b.image =blog_photo
        b.body= textbody

        b.save()
        print("Saved")



    return render(request, 'blog/createblog.html')

def allblogs(request):
    blogs = Blog.objects.all
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def details(request, id):
    blogdetail = get_object_or_404(Blog, pk=id)
    return render(request, 'blog/details.html', {'blog': blogdetail})