from django.shortcuts import render

def home(request):
    return render(request, 'mysite/index.html')

def signup(request):
    return render(request, 'mysite/signup.html')
