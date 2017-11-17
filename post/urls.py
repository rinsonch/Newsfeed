from django.conf.urls import url

from post import views
app_name='posts'
urlpatterns=[
    url(r'^posts/$',views.posts, name='posts'),
    url(r'^search/$',views.Searchview.as_view(),name='search'),
    url(r'^(?P<pk>[0-9]+)/details/$', views.DetailViews.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/comment/$',views.CommentPost.as_view(),name='comment'),
    url(r'^createposts/$',views.CreatePosts.as_view(),name='createposts'),
    url(r'^followlist/$',views.Followlist.as_view(),name='followlist'),
    url(r'^unfollow/$',views.unfollow,name='unfollow'),
    url(r'^follow/$',views.follow,name='follow'),
    url(r'^newsfeed/$',views.newsfeed,name='newsfeed'),
    url(r'^changepic/$',views.changepic,name='changepic'),
    url(r'^like/$',views.like,name='like'),
    url(r'^dislike/$',views.dislike,name='dislike'),
    url(r'^changeprof/$',views.change_prof,name='changeprof'),

    # url(r'^create/(?P<pk>[-\d]+)', views.CreateView.as_view(), name='refresh_post'),
]