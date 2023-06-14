from django.shortcuts import render, redirect
from .models import Registration


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password match a registered user
        if Registration.objects.filter(username=username, password=password).exists():
            return redirect('forms')  # Redirect to the form page after successful login

    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Fix: Use 'username' instead of 'name'
        password = request.POST.get('password')
        # Retrieve other form fields

        registration = Registration(username=username, password=password)
        # Set other field values in the Registration instance

        registration.save()  # Save the registration details in the database
        return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'register.html')


def forms(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        materials_provide = request.POST.getlist('materials_provide')

        # Perform necessary actions with the form data

        return render(request, 'submit.html')

    return render(request, 'forms.html')


def submit(request):
    return render(request, 'submit.html')
