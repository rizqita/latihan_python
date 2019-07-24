from django.shortcuts import render,redirect
from .models import Mentor,Mentee,Blog
from .forms import inputMentee,inputMentor,inputBlog
# Create your views here.
def ata_view_main(request):
    return render(request,'index.html',{})
def author_view(request):
    return render(request,'author.html',{})
def mentor_view(request):
    list_mentor = Mentor.objects.all()
    return render(request,'mentor.html',{'list_mentor':list_mentor})
def mentee_view(request):
    list_mentee = Mentee.objects.all()
    return render(request, 'mentee.html',{'list_mentee':list_mentee})
def blog_view(request):
    list_blog = Blog.objects.all()
    return render(request,'blog.html',{'list_blog':list_blog})
def input_mentee(request):
    if request.method == "POST":
        form = inputMentee(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('http://127.0.0.1:8001/input_mentee')
    else:
        form = inputMentee()
    return render(request,'input_mentee.html',{'form':form})
def input_mentor(request):
    if request.method == "POST":
        form = inputMentor(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('http://127.0.0.1:8001/input_mentor')
    else:
        form = inputMentor()
    return render(request,'input_mentor.html',{'form':form})
def input_blog(request):
    if request.method == "POST":
        form =  inputBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('http://127.0.0.1:8001/input_blog')
    else:
        form = inputBlog()
    return render(request,'input_blog.html',{'form':form})