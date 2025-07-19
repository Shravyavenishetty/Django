from employees.models import Employee
from django.shortcuts import get_object_or_404
from django.shortcuts import render

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  # Fetch the employee by primary key
    context = {
        'employee' : employee,
    }
    return render(request, 'employee_detail.html',context)  # Render the employee detail template with the employee data