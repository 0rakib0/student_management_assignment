from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def StudentList(request):
    students = Student.objects.all()
    return render(request, 'student_management/home.html', context={'students':students})


@login_required
def CreateStudent(request):
    if request.method == 'POST':
        form_data = StudentForm(request.POST, request.FILES)
        
        email = request.POST.get('email')
        roll_number = request.POST.get('roll_number')
        
        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Student already exists with this email!')
            return redirect('student_list')

        if Student.objects.filter(roll_number=roll_number).exists():
            messages.error(request, 'Student already exists with this Roll Number!')
            return redirect('student_list')
            
        
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Student sucessfully added!')
            return redirect('student_list')
        else:
            print(form_data.errors)
            messages.error(request, 'Student not added, Something wrong!')
            
    form = StudentForm()
    return render(request, 'student_management/create_student.html', context={'form':form})


@login_required
def DeleteStudent(request, id):
    try:
        studet = Student.objects.get(id=id)
        studet.delete()
        messages.success(request, 'Student sucessfully deleted!')
        return redirect('student_list')
    except Student.DoesNotExist:
        pass

@login_required  
def UpdateStudent(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        messages.error(request, 'Student Not Found!')
        return redirect('student_list')
    
    if request.method == "POST":
        formdata = StudentForm(request.POST, request.FILES, instance=student)
        if formdata.is_valid():
            formdata.save()
            messages.success(request, 'Student sucessfully Updated!')
            return redirect('student_list')
    form = StudentForm(instance=student)
    return render(request, 'student_management/student_update.html', context={'form':form})
    
