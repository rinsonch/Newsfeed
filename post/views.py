# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Profile
from .forms import UserPosts,Comment,Profilepic
from django.shortcuts import get_object_or_404, redirect,get_list_or_404
from django.views import generic
from .models import NewsFeed,NewsValue
from django.shortcuts import render
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from django.http import request, HttpResponse


# class FullPosts(generic.ListView):
#     template_name = 'posts/userhome.html'
#     model = User
#     context_object_name = 'news'
#
#     def get_queryset(self, *args):
#         return User.object.get(pk=self.request.user.id)

@login_required
def posts(request):
    news=get_object_or_404(User,pk=request.user.id)
    full=get_list_or_404(User)
    return render(request,'posts/userhome.html',{'news':news,'full':full})

class Searchview(generic.ListView):
    model = User
    template_name = 'posts/search_list.html'
    context_object_name = 'user_list'

    def get_queryset(self, *args):
        return User.objects.filter(first_name__icontains=self.request.GET['key']).exclude(username__icontains=self.request.user.username)

class DetailViews(generic.DetailView):
    model=User
    template_name='posts/userdetails.html'

# @receiver(user_logged_in)
class CreatePosts(generic.FormView,generic.ListView):
    form_class = UserPosts
    template_name = 'posts/createdposts.html'
    # success_url = '/posts'
    context_object_name = 'news'

    def get_queryset(self):
        # import pdb
        # pdb.set_trace()
        # form =self.request.GET['content']
        # print form
        q=Profile.objects.get(user_id=self.request.user.id)
        q.newsfeed_set.create(title=self.request.GET['title'],content=self.request.GET['content'])
        # return super(CreatePosts, self).form_valid(form)
        # a=Profile.objects.get(user=self.request.user.id)
        return User.objects.get(pk=self.request.user.id)

    def form_invalid(self, form):
        return redirect("/posts")  # TODO : REMOVE

# def comment(request,pk):
#     if request.method=='POST':
#         form=Comment(request.POST)
#         if form.is_valid():
#             user=form.save()
#             k=Profile.objects.get(user_id)
#         return redirect('/posts/')
#
#     else:
#         form = Comment()

class CommentPost(generic.FormView,generic.ListView):
    form_class = Comment
    template_name = 'posts/commented_posts.html'
    context_object_name = 'a'


    def get_queryset(self):
        a=self.kwargs['pk']
        u=Profile.objects.get(user_id=self.request.user.id)
        k=NewsFeed.objects.get(id=a)
        comment=self.request.GET['comment']
        fed=NewsValue(feedname=k,commented=u,comment=comment)
        fed.save()
        return NewsValue.objects.filter(feedname_id=a)
        # Profile.objects.get(user_id=self.request.user.id).NewsFeed.objects.get(id=a).newsvalue_set.create(comment=comment)
        # return super(Comment, self).form_valid(form)

    def form_invalid(self, form):
        return redirect("/posts")

class Followlist(generic.ListView):
    model=Profile
    template_name='posts/followlist.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return Profile.objects.get(user_id=self.request.user)

def unfollow(request):
    b=request.GET['id']
    p=Profile.objects.get(user_id=request.user.id)
    p.follow.remove(b)
    user = User.objects.get(pk=b)
    return render(request,'posts/followcreated.html',{'user':user,})

def follow(request):
    b=request.GET['id']
    print b
    p = Profile.objects.get(user_id=request.user.id)

    p.follow.add(b)
    user = User.objects.get(pk=b)
    return render(request, 'posts/followcreated.html', {'user': user, })
def like(request):
    b=request.user
    c=request.GET['feedid']
    d=NewsFeed.objects.get(id=c)
    if(b in d.dislike.all()):
        d.dislike.remove(b)
    else:
        d.like.add(b)
    return render(request,'posts/likes.html',{'a':d,})
def dislike(request):
    # import pdb
    # pdb.set_trace()
    b = request.user
    c = request.GET['feedid']
    d = NewsFeed.objects.get(id=c)
    if b in d.like.all():
        d.like.remove(b)
    else:
        d.dislike.add(b)
    return render(request, 'posts/likes.html', {'a': d, })

def newsfeed(request):
    a= Profile.objects.get(user_id=request.user.id)
    c=a.follow.all()

    print c
    list1 = [i.profile.id for i in c]
    print list1
    news=NewsFeed.objects.filter(userid_id__in=list1).order_by('-pub_date')

    return render(request,'posts/newsfeed.html',{'news':news,})

def changepic(request):
    a=Profile.objects.get(user_id=request.user.id)
    return render(request,'posts/changepic.html',{'a':a,})

def change_prof(request):
    import pdb
    pdb.set_trace()
    if request.method == 'POST':
        form =Profilepic(request.POST, request.FILES)
        if form.is_valid():
            editprofile = form.save(commit=False)
            print request.user.id
            editprofile.user.id=request.user.id
            editprofile.user.dob=request.user.profile.dob
            editprofile.save()
            return redirect('posts/changepic.html')

    return redirect('post/changepic.html')

class CreateView(generic.DetailView):
    template_name = 'posts/createdposts.html'
    model = NewsFeed
    context_object_name = 'news'
# class NewsSearchView(ListView):
#     model = News
#     template_name = 'results.html'
#     context_object_name = 'results'
#
#     def get_queryset(self, **kwargs):
#         if self.request.is_ajax():
#             q = self.request.GET.get('q')
#             if q is not None:
#                 return News.objects.filter(
#                     Q(title__icontains=q)).order_by('-pub_date')
#
#
#
#




