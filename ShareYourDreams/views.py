from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm, RegistrationForm
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def dreams_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ShareYourDreams/dreams_list.html', {'posts': posts})


def dream_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'ShareYourDreams/dream_detail.html', {'post': post})


def dream_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ShareYourDreams.views.dream_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'ShareYourDreams/dream_edit.html', {'form': form})


def dream_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ShareYourDreams.views.dream_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'ShareYourDreams/dream_edit.html', {'form': form})


def registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'ShareYourDreams/registration.html', {'form': form})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return HttpResponse("Registration successful!!!.")
        else:
            return HttpResponse("Form is invalid you cocksucker!!!.")
    return HttpResponse("Suck my cock!!!.")
