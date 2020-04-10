from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {'title':'about'})

def about(request):
    return render(request, 'blog/about.html')