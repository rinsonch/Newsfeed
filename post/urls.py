from django.conf.urls import url

from post import views
app_name='posts'
urlpatterns=[
    url(r'^posts/$',views.PostsView.as_view(), name='posts'),
    url(r'^search/$',views.Searchview.as_view(),name='search'),
    url(r'^(?P<pk>[0-9]+)/details/$', views.DetailViews.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/comment/$',views.CommentPost.as_view(),name='comment'),
    url(r'^createposts/$',views.CreatePostView.as_view(),name='createposts'),
    url(r'^followlist/$',views.Followlist.as_view(),name='followlist'),
    url(r'^unfollow/$',views.UnfollowView.as_view(),name='unfollow'),
    url(r'^follow/$',views.FollowView.as_view(),name='follow'),
    url(r'^newsfeed/$',views.PageView.as_view(),name='newsfeed'),
    url(r'^like/$',views.like,name='like'),
    url(r'^dislike/$',views.dislike,name='dislike'),
    # url(r'^changeprof/$',views.change_prof,name='changeprof'),


]