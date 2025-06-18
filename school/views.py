from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import *
from .forms import *

@login_required(login_url='my-login')  
def admin_dashboard(request):
    user = request.user  
    context = {'user': user}
    return render(request, 'school/admin-dashboard.html', context)

@login_required(login_url='my-login')
def academic_session(request):
    session = AcademicSession.objects.all()
    form = AcademicSessionForm()
    if request.method == "POST":
        form = AcademicSessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New session created successfully.")
            return redirect('academic-session')
        else:
            messages.error(request, 'This Session Already Exists')

    context = {'sessions': session, 'form': form}
    return render(request, 'school/academic-session.html', context)


@login_required(login_url='my-login')
def add_subject(request):
    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-subject')

    subjects = Subject.objects.select_related('section').all().order_by('section__name', 'name')
    sections = [ 'Senior', 'Junior','Nursery','Primary' ]

    context = {
        'subjects': subjects,
        'sections': sections,
        'form': form
    }
    return render(request, 'school/add-subject.html', context)

@login_required(login_url='my-login')
def add_teacher(request):
    form = TeacherForm()
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')
        else:
            return HttpResponse("Can't save this form")

    context = {'form': form}
    return render(request, 'school/teachers/add-teacher.html', context)


@login_required(login_url='my-login')
def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers':teachers}
    return render(request, 'school/teachers/teacher-list.html', context)

@login_required(login_url='my-login')
def teacher_detail(request, pk):
    teacher = Teacher.objects.get(id=pk)
    context ={'teacher':teacher}
    return render(request, 'school/teachers/teacher-detail.html', context)





@login_required(login_url='my-login')
def logoutUser(request):
    auth.logout(request)
    return redirect('my-login')
