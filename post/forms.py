from django import forms
from home.models import Profile
from post.models import NewsFeed
from .models import NewsValue

class UserPosts(forms.ModelForm):
    class Meta:
        model=NewsFeed
        fields=['title','content','feedpic']

class Comment(forms.ModelForm):
    class Meta:
        model=NewsValue
        fields=['comment']

class Profilepic(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profpic']
