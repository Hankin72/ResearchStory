from django.shortcuts import render

# Create your views here.

def index(request):
    """homepage"""

    return render(request, 'MainPage/index.html')