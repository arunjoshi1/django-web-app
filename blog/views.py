from django.shortcuts import render,redirect
from .models import Post
from .forms import Post_form
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from django.contrib import messages
# Create your views here.
def home(request):
    posts=Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 12)  # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html',{'posts':posts})

def view_post(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post.html',{'post':post})



def about(request):
    return render(request,'about.html')



def contact(request):
    return render(request,'contact.html')



def edit_post(request,id):
    instance=Post.objects.get(id=id)
    if request.method=='POST' :
        form=Post_form(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = Post_form(instance=instance)
    return render(request,'edit-post.html',{'form':form})


def delete(request,id):
    obj=Post.objects.get(id=id).delete()
    return redirect(home)

@login_required(login_url='login')
def create_post(request):
    if request.method=='POST':
        form=Post_form(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('home')
    form =Post_form()
    return render(request,'create.html',{'form':form})


def search(request):
    query = request.GET.get('s')
    data_title = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request,'search.html',{'data':data_title})

def my_post(request):
    data=Post.objects.all().order_by('-date')
    return render(request,'mypost.html',{'data':data})