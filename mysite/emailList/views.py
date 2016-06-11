from django.shortcuts import render, redirect
from mysite.models import Email

def home(request):
    return render(request, 'mysite/index.html')

def signup(request):
    return render(request, 'mysite/signup.html')

def email(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')

    names = name.split()
    first_name = names[0]
    last_name = names[-1]
    if len(names) == 3:
        middle_name = names[1]
    else:
        middle_name = ""

    print(first_name, middle_name, last_name, email)

    record = Email.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email)
    record.save()

    return redirect('/')
