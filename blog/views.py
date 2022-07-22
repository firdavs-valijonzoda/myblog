from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/index.html',  {'posts': posts})