from django.shortcuts import render, redirect

def home(request):
    return render(request, 'mysite/index.html')

def signup(request):
    return render(request, 'mysite/signup.html')

def email(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    print(name)
    print(email)

    return redirect('/')
