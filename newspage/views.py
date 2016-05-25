from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

def index(request):
    return render(request, 'newspage/index.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'newspage/post_detail.html', {
        'post':post,
        })