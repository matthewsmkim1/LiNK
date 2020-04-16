from django.shortcuts import render

# Create your views here.


def testy(request):
    return render(request, 'frontend/index.html')
