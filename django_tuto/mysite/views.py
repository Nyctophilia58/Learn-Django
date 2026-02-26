from django.shortcuts import render
from employees.models import Employee

def home(request):
    employees = Employee.objects.all()
    bio = 'Hello there this is a demo bio to check if words are truncated or not'
    context = {
        'employees': employees,
        'bio' : bio
    }
    return render(request, 'home.html', context)
