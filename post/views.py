# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from home.models import Profile
from .forms import Comment,Profilepic
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.generic import FormView,ListView,DetailView
from .models import NewsFeed,NewsValue
from django.shortcuts import render


class PostsView(ListView):
    template_name = 'posts/userhome.html'
    model = User
    context_object_name = 'news'

    def get_queryset(self):
        news=get_object_or_404(User,pk=self.request.user.id)
        return news


class Searchview(ListView):
    model = User
    template_name = 'posts/search_list.html'
    context_object_name = 'user_list'

    def get_queryset(self, *args):
        set=User.objects.filter(email__icontains=self.request.GET['key'])|User.objects.filter(first_name__icontains=self.request.GET['key'])
        qset=set.exclude(username__icontains=self.request.user.username)
        return qset


class DetailViews(DetailView):
    model=User
    template_name='posts/userdetails.html'


class CreatePostView(FormView):
    template_name = 'posts/createdposts.html'

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            q = Profile.objects.get(user_id=request.user.id)
            if request.FILES:
                q.newsfeed_set.create(title=request.POST['title'],
                                      content=request.POST['content'], feedpic=request.FILES['file'])
            else:
                q.newsfeed_set.create(title=request.POST['title'],
                                      content=request.POST['content'])
        a = Profile.objects.get(user_id=request.user.id)
        c = a.follow.all()
        list1 = [i.profile.id for i in c]
        news = NewsFeed.objects.filter(userid_id__in=list1).order_by('-pub_date')
        return render(request,'posts/createdposts.html',{'news':news,})


class CommentPost(FormView,ListView):
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


    def form_invalid(self, form):
        return redirect("/posts")


class Followlist(ListView):
    model=Profile
    template_name='posts/followlist.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return Profile.objects.get(user_id=self.request.user)


class UnfollowView(FormView):

    def get(self, request, *args, **kwargs):
        b = request.GET['id']
        p = Profile.objects.get(user_id=request.user.id)
        p.follow.remove(b)
        user = User.objects.get(pk=b)
        return render(request, 'posts/followcreated.html', {'user': user, })


class FollowView(FormView):
    template_name = 'posts/followcreated.html'

    def get(self, request, *args, **kwargs):
        b = request.GET['id']
        p = Profile.objects.get(user_id=request.user.id)
        p.follow.add(b)
        user = User.objects.get(pk=b)
        return render(request, 'posts/followcreated.html', {'user': user, })


class PageView(generic.ListView):
    paginate_by = 5
    model = NewsFeed
    context_object_name = 'news'
    template_name = 'posts/newsfeed.html'

    def get_queryset(self):
        a = Profile.objects.get(user_id=self.request.user.id)
        c = a.follow.all()
        list1 = [i.profile.id for i in c]
        return NewsFeed.objects.filter(userid_id__in=list1).order_by('-pub_date')


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
    b = request.user
    c = request.GET['feedid']
    d = NewsFeed.objects.get(id=c)
    if b in d.like.all():
        d.like.remove(b)
    else:
        d.dislike.add(b)
    return render(request, 'posts/likes.html', {'a': d, })

# def newsfeed(request):
#     a= Profile.objects.get(user_id=request.user.id)
#     c=a.follow.all()
#     list1 = [i.profile.id for i in c]
#     news=NewsFeed.objects.filter(userid_id__in=list1).order_by('-pub_date')
#
#     return render(request,'posts/newsfeed.html',{'news':news,})


# def change_prof(request):
#     import pdb
#     pdb.set_trace()
#     if request.method == 'POST':
#         form =Profilepic(request.POST, request.FILES)
#         if form.is_valid():
#             editprofile = form.save(commit=False)
#             editprofile.user.id=request.user.id
#             editprofile.user.dob=request.user.profile.dob
#             editprofile.save()
#             return redirect('posts/changepic.html')
#
#     return redirect('post/changepic.html')





# @login_required
# def posts(request):
#     news=get_object_or_404(User,pk=request.user.id)
#     full=get_list_or_404(User)
#     return render(request,'posts/userhome.html',{'news':news,'full':full})




# def createposts(request):
#     if(request.method=='POST'):
#         q = Profile.objects.get(user_id=request.user.id)
#         if request.FILES:
#             q.newsfeed_set.create(title=request.POST['title'],
#             content=request.POST['content'],feedpic=request.FILES['file'])
#         else:
#             q.newsfeed_set.create(title=request.POST['title'],
#                                   content=request.POST['content'])
#     a = Profile.objects.get(user_id=request.user.id)
#     c = a.follow.all()
#     list1 = [i.profile.id for i in c]
#     news = NewsFeed.objects.filter(userid_id__in=list1).order_by('-pub_date')
#     return render(request,'posts/createdposts.html',{'news':news,})

