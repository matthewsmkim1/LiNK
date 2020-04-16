from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import LinkGroup
from users.models import Profile
from .forms import LinkGroupCreationForm, LinkGroupJoinForm
# Create your views here.
import bcrypt
import random
import string


def randomString(stringLength=50):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


@login_required
def create_group(request):
    current_user = request.user.username
    if request.method == "POST":
        group_creation_form = LinkGroupCreationForm(request.POST)
        if group_creation_form.is_valid():
            salt = bcrypt.gensalt()
            key = randomString()
            encoded = key.encode()
            hashed = bcrypt.hashpw(encoded, salt)

            new_group = LinkGroup.objects.create(
                group_name=group_creation_form.cleaned_data['group_name'],
                group_description=group_creation_form.cleaned_data['group_description'],
                bkey=hashed
            )
            user = Profile.objects.get(user=request.user)
            new_group.members.add(user)
            new_group.save()
            messages.success(
                request, f"This is your group's join key. Make sure to keep it somewhere safe! \n {key} \n \
                 \n If you want to add someone to the group, give them the key and the group name\n {group_creation_form.cleaned_data['group_name']}")
            return redirect('profile')

        # return redirect('/show_group)
    else:
        group_creation_form = LinkGroupCreationForm()
        context = {
            "group_creation_form": group_creation_form
        }
        return render(request, 'groups/create_group.html', context)


def test_react(request):
    return render(request, 'groups/test_react.html')

#! TODO
@login_required
def show_group(request, groupname):
    current_user = request.user.username


#! TODO
@login_required
def add_post_to_group(request, groupname):
    current_user = request.user.username

#! TODO
@login_required
def create_post_in_group(request, groupname):
    current_user = request.user.username


def add_user_to_group(request, group):
    user = Profile.objects.get(user=request.user)
    group.members.add(user)


@login_required
def join_group(request):
    current_user = request.user.username
    if request.method == "POST":
        group_join_form = LinkGroupJoinForm(request.POST)
        if group_join_form.is_valid():
            key = group_join_form.cleaned_data['key']
            group_name = group_join_form.cleaned_data['group_name']
            group = LinkGroup.objects.get(group_name=group_name)

            if bcrypt.checkpw(key.encode(), group.bkey):
                add_user_to_group(request, group)
                messages.success(
                    request, f"You have been successfully added to the group {group_name}!")
                return redirect('profile')
            else:
                messages.failure(
                    request, f"Sorry, that key and or group name is not correct")
                group_join_form = LinkGroupJoinForm()
                context = {
                    "group_join_form": group_join_form
                }
                return render(request, 'groups/join_group.html', context)

        # return redirect('/show_group)
    else:
        group_join_form = LinkGroupJoinForm()
        context = {
            "group_join_form": group_join_form
        }
        return render(request, 'groups/join_group.html', context)


#! TODO after admin functionality is added to group so the admin can change things, such as the group avatar
@login_required
def edit_group_details(request):
    current_user = request.user.username


#! TODO after admin functionality is added to group so the admin can change things, such as the group avatar
@login_required
def edit_group_announcements(request):
    current_user = request.user.username


#! TODO after admin functionality is added to group so the admin can change things, such as the group avatar
@login_required
def edit_group_calendar(request):
    current_user = request.user.username
