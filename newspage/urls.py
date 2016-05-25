from django.conf.urls import url


urlpatterns = [

    url(r'^$','newspage.views.index', name="index"),

]