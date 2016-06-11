from django.shortcuts import render, redirect
from emailList.models import Email

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

    if len(names) == 1:
        last_name = ""

    for each in first_name, middle_name, last_name:
        small = each.lower()                        # Convert string to lower case
        each = small[0].upper() + small[1:].lower() # Format data ready for storing in database

    print(first_name, middle_name, last_name, email)

    record = Email.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email)
    record.save()

    return redirect('/')
