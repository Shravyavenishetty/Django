from django.shortcuts import render
from employees.models import Employee

def home(request):
    employess = Employee.objects.all()  # Fetch all employees from the database
    context = {
        'employees': employess, # Pass the employees to the template context
    }
    return render(request, 'home.html', context)  # Render the home template with the context