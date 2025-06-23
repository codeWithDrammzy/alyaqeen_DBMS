from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

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
        students = Student.objects.filter(student_class__name__startswith='SS')  # <-- FIXED

    senior_classes = SchoolClass.objects.filter(name__startswith='SS')

    context = {
        "students": students,
        "senior_classes": senior_classes,
        "selected_class": class_filter,
    }
    return render(request, 'school/students/senior-class.html', context)


@login_required(login_url='my-login')
def juniorclass(request):
    class_filter = request.GET.get('class')

    # ✅ Get all junior classes from SchoolClass model
    junior_classes = SchoolClass.objects.filter(name__startswith='JSS').order_by('name')

    # ✅ Filter students by selected class or show all JSS students
    if class_filter:
        students = Student.objects.filter(student_class__name__iexact=class_filter)
    else:
        students = Student.objects.filter(student_class__name__icontains='JSS')

    context = {
        'students': students,
        'selected_class': class_filter,
        'junior_classes': junior_classes,
    }
    return render(request, 'school/students/Junior-class.html', context)


@login_required(login_url='my-login')
def primaryclass(request):
    class_filter = request.GET.get('class')

    # ✅ Get all junior classes from SchoolClass model
    primary_classes = SchoolClass.objects.filter(name__startswith='Pr').order_by('name')

    # ✅ Filter students by selected class or show all JSS students
    if class_filter:
        students = Student.objects.filter(student_class__name__iexact=class_filter)
    else:
        students = Student.objects.filter(student_class__name__icontains='Primary')

    context = {
        'students': students,
        'selected_class': class_filter,
        'primary_classes': primary_classes,
    }
    return render(request, 'school/students/primary-class.html', context)


@login_required(login_url='my-login')
def nurseryclass(request):
    class_filter = request.GET.get('class')

    # ✅ Get all junior classes from SchoolClass model
    nursery_classes = SchoolClass.objects.filter(name__startswith='Nu').order_by('name')

    # ✅ Filter students by selected class or show all JSS students
    if class_filter:
        students = Student.objects.filter(student_class__name__iexact=class_filter)
    else:
        students = Student.objects.filter(student_class__name__icontains='Nursery')

    context = {
        'students': students,
        'selected_class': class_filter,
        'nursery_classes': nursery_classes,
    }
    return render(request, 'school/students/nursery-class.html', context)





@login_required(login_url='my-login')
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student_class_name = student.student_class.name  # e.g. "JSS 1", "SS 2", etc.

    # Store the class before deleting
    class_redirect = None
    if 'JSS' in student_class_name:
        class_redirect = reverse('junior-class') + f"?class={student_class_name}"
    elif 'SS' in student_class_name:
        class_redirect = reverse('senior-class') + f"?class={student_class_name}"
    elif 'Primary' in student_class_name or 'PR' in student_class_name.upper():
        class_redirect = reverse('primary-class') + f"?class={student_class_name}"

    student.delete()

    if class_redirect:
        return redirect('admin-dashboard')
    return redirect('admin-dashboard')  
