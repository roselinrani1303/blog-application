from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse
from django.db import IntegrityError


# View for adding an employee
def add_employee(request):
    if request.method == 'POST':
        empid = request.POST['id']
        empname = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']

        try:
            # Insert new employee into the database
            employee = Employee(
                empid=empid,
                empname=empname,
                email=email,
                contact=contact
            )
            employee.save()
            return redirect('employee_list')  # Redirect to employee list page
        except IntegrityError:
            return HttpResponse("Error: Unable to save employee.", status=400)

    return render(request, 'add_employee.html')


# View for listing all employees
def employee_list(request):
    employees = Employee.objects.all()  # Get all employee records from the database
    return render(request, 'employee_list.html', {'employees': employees})


# View for deleting an employee
def delete_employee(request, empid):
    try:
        employee = Employee.objects.get(empid=empid)
        employee.delete()  # Delete the employee
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found", status=404)
    
    return redirect('employee_list')  # Redirect to employee list page after deletion


# View for updating an employee's information
def update_employee(request, empid):
    try:
        employee = Employee.objects.get(empid=empid)  # Get the employee object

        if request.method == 'POST':
            # Update employee fields from the form data
            employee.empname = request.POST['name']
            employee.email = request.POST['email']
            employee.contact = request.POST['contact']
            employee.save()  # Save updated employee details

            return redirect('employee_list')  # Redirect after update

        return render(request, 'update_employee.html', {'employee': employee})
    
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found", status=404)

