from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post3

# Create your views here.

def post_list7(request):

    posts = Post3.objects.all()
    
    return render(request, 'lk/post_list3.html', {'posts': posts})

def post_list(request):

    posts = Post3.objects.all()
    context_dict = {'posts': posts}
    return render(request, 'lk/post_list3.html', context_dict)

def post_detail(request, pk):
    post = get_object_or_404(Post3, pk=pk)
    return render(request, 'lk/post_detail3.html', {'post': post})
