from django.shortcuts import render,redirect
from .models import Hewan
from .forms import inputHewan


# Create your views here.
def daftar_binatang(request):
    list_hewan = Hewan.objects.all()
    return render(request,'daftar_binatang.html',{'list_hewan':list_hewan})
def twitter(request):
    return render(request,'twitter.html',{})
def input_hewan(request):
    if request.method == "POST":
        form = inputHewan(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('http://127.0.0.1:8001/input_hewan')
    else:
        form = inputHewan()
    return render(request,'input_hewan.html',{'form':form})