from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django import forms
from groups.models import LinkGroup
from .models import Post
from users.models import Profile
import os

def user_videos(request):
    return render(request, 'journal/user_videos.html')

def user_photos(request):
    return render(request, 'journal/user_photos.html')

def user_search(request):
    return render(request, 'journal/user_search.html')


class GroupPostListView(ListView):
    model = Post
    template_name = 'journal/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        groupname = get_object_or_404(LinkGroup, group_name=self.kwargs.get('groupname'))
        return Post.objects.filter(group_to_post=groupname)

        # return groupname.posts.all()


class PostListView(ListView):
    model = Post
    template_name = 'journal/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Post.objects.filter(group_to_post=user.profile.current_group_for_user)



class UserPostListView(ListView):
    model = Post
    template_name = 'journal/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

#
# class PostCreateForm(forms.Form):
#     # name = forms.CharField()
#     # message = forms.CharField(widget=forms.Textarea)
#     title = forms.CharField(max_length=100)
#     # content = forms.CharField(max_length=100)
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'image', 'video', 'group_to_post']


# class TempGroupView(LoginRequiredMixin, CreateView):
#     model = Profile
#     fields = ['current_group_for_user']
#
#     def get_success_url(self):
#         return 'http://127.0.0.1:8000/'
#
#     def form_valid(self, form):
#         print(self.request.user)
#         print(form.instance.user)
#         form.save()
#         return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # form_class = PostCreateForm
    fields = [ 'title', 'content', 'image', 'group_to_post']
    #
    # def group_shit(self, form):
    #never called
    #     print('2222222222222')
    #     print(form.instance.group_to_post)

    def form_valid(self, form):
        form.instance.author = self.request.user
        # print(form.instance.group_to_post)
        # form.instance.group_to_post = self.request.current_group????
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = [ 'title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'journal/about.html', {'title': 'About'})
