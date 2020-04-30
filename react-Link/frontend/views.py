# Create your views here.
from django.shortcuts import render
from django.views.generic.detail import DetailView

from posts.models import Post


def index(request):
    return render(request, 'frontend/index.html')


class PostDetailView(DetailView):
    model = Post
    template_name = 'frontend/index.html'
