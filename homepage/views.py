from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):

    current_user = get_user(request)
    form = PostForm(initial={'author':current_user})

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    posts = Post.objects.all().order_by('-created_date')
    context = {'posts': posts, 'form': form}
    return render(request, 'homepage/home.html', context)

