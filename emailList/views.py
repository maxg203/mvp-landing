from django.shortcuts import render, redirect
from emailList.models import Email

def home(request):
    return render(request, 'emailList/index.html')

def signup(request):
    return render(request, 'emailList/signup.html')

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

    if len(names) == 1:
        last_name = ""

    small = first_name.lower()
    first_name = small[0].upper() + small[1:]

    try:
        small = middle_name.lower()
        middle_name = small[0].upper() + small[1:]
    except:
        middle_name = ""

    try:
        small = last_name.lower()
        last_name = small[0].upper() + small[1:]
    except:
        last_name = ""
        
    record = Email.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email)
    record.save()

    return redirect('/')
