from employees.models import Employee
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  # Fetch the employee by primary key
    return HttpResponse(f"Employee: {employee.first_name} {employee.last_name}, Designation: {employee.designation}")  # Return a simple response with employee details