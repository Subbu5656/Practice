from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def Base(request):
	msg = 'Welcome To My World'
	return HttpResponse(msg)

def New(request):
	return render(request, 'employee/new.html')

def Home(request):
	return render(request, 'employee/home.html')

def Main(request):
	return render(request, 'employee/base.html')

def Save(request):
	if request.method == 'POST':
		emp = Employee(
			name = request.POST['name'],
			company = request.POST['company'],
			location = request.POST['location'],
			salary = float(request.POST['salary'])
			)
		emp.save()
	return redirect('/employee/details/')
def AllEmp(request):
	data = Employee.objects.all()
	return render(request, 'employee/details.html', {'data':data})

def Update(request, id):
	emp = Employee.objects.get(id=id)
	if request.method == 'POST':
		emp.name = request.POST['name']
		emp.section = request.POST['company']
		emp.location = request.POST['location']
		emp.marks = request.POST['salary']
		emp.save()
	return redirect('/employee/details/')

def Home1(request, id):
	emp = Employee.objects.get(id=id)
	return render(request, 'employee/home.html', {'emp':emp})
def Delete(request, id):
	emp = Employee.objects.get(id=id).delete()
	return redirect('/employee/details/')









