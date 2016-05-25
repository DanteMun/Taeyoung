from django.conf.urls import url


urlpatterns = [

    url(r'^$','newspage.views.index', name="index"),
    url(r'^(?P<pk>\d+)/$', 'newspage.views.post_detail', name="post_detail"),
    url(r'^new/$', 'newspage.views.post_new', name="post_new"),
]