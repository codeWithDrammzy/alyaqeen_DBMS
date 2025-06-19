from django.shortcuts import render, redirect
from .forms import*
from django.contrib.auth.decorators import login_required


@login_required(login_url='my-login')
def add_student(request):
    if request.method == "POST":
        guardian_form = GuardianForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)
        
        if guardian_form.is_valid() and student_form.is_valid():
            guardian = guardian_form.save()
            student = student_form.save(commit=False)
            student.guardian = guardian
            student.save()
            return redirect('admin-dashboard')  
    else:
        guardian_form = GuardianForm()
        student_form = StudentForm()

    return render(request, 'school/students/add-student.html', {
        'guardian_form': guardian_form,
        'student_form': student_form
    })

@login_required(login_url='my-login')
def student_list(request):
    students = Student.objects.all()
    context ={'students':students}
    return render(request, 'school/students/student-list.html', context)

@login_required(login_url='my-login')
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'school/students/student-detail.html', context)