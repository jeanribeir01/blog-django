from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5

def index(request):
    return render(
        request,
        'blog/index.html',
        {'posts': Post.objects.all()}
    )

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )

