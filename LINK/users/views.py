from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UpdateCurrentGroupForm
from .models import Profile
from groups.models import LinkGroup


def members_group(request):
    return render(request, 'users/members_group.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def change_group(request):
    if request.method == 'POST':
        change_group_form = UpdateCurrentGroupForm(
            request.POST, instance=request.user.profile)

        if change_group_form.is_valid():
            change_group_form.save()
            groupname = request.user.profile.current_group_for_user.group_name
            messages.success(
                request, f'You have changed the group you are viewing to ' + groupname)
    else:
        change_group_form = UpdateCurrentGroupForm(
            instance=request.user.profile)

    profile = Profile.objects.get(user=request.user)
    groups = list(profile.groups.all())
    all_groups = LinkGroup.objects.all()

    counter = 1
    counts = []
    for group in all_groups:
        if counter == 4:
            counter = counter + 1
        counts.append(counter)
        counter = counter + 1

    zipped = list(zip(all_groups, counts))

    actual_counts = []
    for tup in zipped:
        g = tup[0]
        if g in groups:
            actual_counts.append(tup[1])

    group_strings = []
    for group in groups:
        group_strings.append(str(group))

    listy = list(zip(group_strings, actual_counts))

    context = {
        'change_group_form': change_group_form,
        'groups_list': listy
    }

    return render(request, 'users/change_group.html', context)
