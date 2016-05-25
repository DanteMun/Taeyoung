from django.conf.urls import url


urlpatterns = [

    url(r'^$','newspage.views.index', name="index"),
    url(r'^(?P<pk>\d+)/$', 'newspage.views.post_detail', name="post_detail"),
    url(r'^new/$', 'newspage.views.post_new', name="post_new"),
    url(r'^(?P<post_pk>\d+)/comment/new/$', 'newspage.views.comment_new', name="comment_new"),
]