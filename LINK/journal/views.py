from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Journal Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Journal Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'journal/home.html', context)


def about(request):
    return render(request, 'journal/about.html', {'title': 'About'})
