from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'newspage/index.html', {
        'post_list': post_list,
        })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'newspage/post_detail.html', {
        'post':post,
        })

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'newspage/post_new.html', {
        'form' : form,
        })