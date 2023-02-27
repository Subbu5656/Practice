from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def Home(request):
	return render(request, 'student/home.html')

def New(request):
	if request.method == 'POST':
		std = Student(
			name = request.POST['name'],
			section = request.POST['section'],
			location = request.POST['location'],
			marks = float(request.POST['marks'])
			)
		std.save()
	return redirect('/student/details/')
def AllStd(request):
	data = Student.objects.all()
	return render(request, 'student/details.html', {'data':data})

def Update(request, id):
	std = Student.objects.get(id=id)
	if request.method == 'POST':
		std.name = request.POST['name']
		std.section = request.POST['section']
		std.location = request.POST['location']
		std.marks = request.POST['marks']
		std.save()
	return redirect('/student/details/')

def Home1(request, id):
	std = Student.objects.get(id=id)
	return render(request, 'student/home.html', {'std':std})
def Delete(request, id):
	std = Student.objects.get(id=id).delete()
	return redirect('/student/details/')













