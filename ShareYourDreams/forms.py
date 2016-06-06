from django import forms
from .models import Post
from django.contrib.auth.models import User


from django.contrib.auth.forms import UserCreationForm


# todo suck my dick
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoggingInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
