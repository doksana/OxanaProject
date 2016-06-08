from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm, RegistrationForm, LoggingInForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.
def dreams_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ShareYourDreams/dreams_list.html', {'posts': posts})


def dream_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'ShareYourDreams/dream_detail.html', {'post': post})


# todo auth
# https://docs.djangoproject.com/ja/1.9/topics/auth/default/#authentication-in-web-requests
def dream_new(request):
    if request.user.is_authenticated():
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
        return render(request, 'ShareYourDreams/dream_new.html', {'form': form})
    else:
        return HttpResponse("Authenticate to create new post!")


# todo auth
# https://docs.djangoproject.com/ja/1.9/topics/auth/default/#authentication-in-web-requests
def dream_edit(request, pk):
    if request.user.is_authenticated():
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
    else:
        return HttpResponse("Authenticate to edit this post!")


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


def logging_in(request):
    if request.method == "GET":
        form = LoggingInForm()
        return render(request, 'ShareYourDreams/logging_in.html', {'form': form})
    elif request.method == "POST":
        form = LoggingInForm(request.POST)
        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                return HttpResponse("User is valid, active and authenticated")
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            return HttpResponse("The username and password were incorrect.")


def logging_out(request):
    logout(request)
    if request.user.is_authenticated():
        return HttpResponse ("You are still logged in!")
    elif request.user.is_anonymous():
        return HttpResponse('You loged out and are anonymous now')

