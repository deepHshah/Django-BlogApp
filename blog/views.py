from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import *

def main(request):
    return render(request,"main.html")

def home(request):
    data = Post.objects.all()
    return render(request,"home.html",context={"data":data})

#def login(request):
    #return render(request,"login.html")
def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'home.html')   
    return render(request, "login.html")

def register(request):
    if request.method=="POST":   
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')  
    return render(request, "register.html")

def signout(request):
    logout(request)
    return redirect("/")

def addblog(request):
    if request.method=="POST":
        form = BlogPostFrom(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "addblog.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostFrom()
    return render(request, "addblog.html", {'form':form})

def Profile(request):
    return render(request,"profile.html")

def Delete(request,user_id):
    user_id = int(user_id)
    try:
        blogpost = blogpost.objects.get(id = book_id)
    except blogpost.DoesNotExist:
        return redirect('/')
    blogpost.delete()
    return redirect('/')

@login_required
def edit_blog(request, blog_id):
    blogpost = get_object_or_404(Post, id=blog_id, author=request.user)

    if request.method == "POST":
        form = BlogPostFrom(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post updated successfully!")
            return redirect("home")
    else:
        form = BlogPostFrom(instance=blogpost)

    return render(request, "edit_blog.html", {"form": form, "blogpost": blogpost})
