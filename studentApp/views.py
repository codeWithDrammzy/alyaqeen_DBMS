from django.shortcuts import render, redirect, get_object_or_404
from .forms import*
from django.contrib.auth.decorators import login_required
from .models import*


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
            return redirect('add-student')  
    else:
        guardian_form = GuardianForm()
        student_form = StudentForm()

    return render(request, 'school/students/add-student.html', {
        'guardian_form': guardian_form,
        'student_form': student_form
    })


@login_required(login_url='my-login')
def student_list(request):
    class_filter = request.GET.get('class')

    if class_filter == 'senior':
        students = Student.objects.filter(student_class__name__icontains='SS')
    elif class_filter == 'junior':
        students = Student.objects.filter(student_class__name__icontains='JSS')
    elif class_filter == 'primary':
        students = Student.objects.filter(student_class__name__icontains='Primary')
    elif class_filter == 'nursery':
        students = Student.objects.filter(student_class__name__icontains='Nursery')
    else:
        students = Student.objects.all()

    context = {'students': students}
    return render(request, 'school/students/student-list.html', context)


@login_required(login_url='my-login')
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'school/students/student-detail.html', context)


def edit_student(request, pk):
    student =Student.objects.get(id=pk)
    guardian = student.guardian  # adjust this based on your model relationship

    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        guardian_form = GuardianForm(request.POST, instance=guardian)

        if student_form.is_valid() and guardian_form.is_valid():
            guardian_form.save()
            student_form.save()
            return redirect('student-detail', pk=student.id)
    else:
        student_form = StudentForm(instance=student)
        guardian_form = GuardianForm(instance=guardian)

    return render(request, 'school/students/edit-student.html', {
        'student_form': student_form,
        'guardian_form': guardian_form
    })


@login_required(login_url='my-login')
def seniorclass(request):
    class_filter = request.GET.get('class')  # e.g., 'SS 1'

    if class_filter:
        students = Student.objects.filter(student_class__name__iexact=class_filter)
    else:
        students = Student.objects.filter(student_class__name__icontains='SS')

    senior_classes = SchoolClass.objects.filter(name__startswith='SS')

    context = {
        "students": students,
        "senior_classes": senior_classes,
        "selected_class": class_filter,
    }
    return render(request, 'school/students/senior-class.html', context)




@login_required(login_url='my-login')
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student-list')