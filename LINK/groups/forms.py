from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import LinkGroup
from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField


class LinkGroupCreationForm(ModelForm):

    class Meta:
        model = LinkGroup
        fields = [
            "group_name",
            "group_description",
        ]
        widgets = {}


class LinkGroupJoinForm(ModelForm):

    bkey = forms.TextInput()

    class Meta:
        model = LinkGroup
        fields = [
            "group_name",
        ]
        widgets = {}

