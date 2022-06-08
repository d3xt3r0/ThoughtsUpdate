from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user, authenticate, login, logout
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):

    current_user = request.user
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form_model = form.save(commit=False)
            form_model.author= current_user
            form_model.save()
            return redirect('index')

    posts = Post.objects.all().order_by('-created_date')
    context = {'posts': posts, 'form': form}
    return render(request, 'homepage/home.html', context)


def login_view(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password, incorrect')

    context = {}
    return render(request, 'homepage/login_register.html', context)

