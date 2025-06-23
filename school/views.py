from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.models import auth
from django.db.models import Q
from django.contrib import messages
from .models import *
from studentApp.models  import*
from .forms import *

@login_required(login_url='my-login')  
def admin_dashboard(request):
    total_student = Student.objects.count()
    total_teacher = Teacher.objects.count()
    user = request.user  
    context = {'user': user,
               'total_student':total_student,
               'total_teacher':total_teacher
               
               }
    return render(request, 'school/admin/admin-dashboard.html', context)



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
    return render(request, 'school/admin/academic-session.html', context)


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
    return render(request, 'school/admin/add-subject.html', context)

@login_required(login_url='my-login')
def remove_subject(request, pk):
    subject = Subject.objects.get(id = pk)
    subject.delete()
    return redirect('add-subject')

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
def edit_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)
    if request.method == "POST":
        form  = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')

    return render(request, 'school/teachers/edit-teacher.html', {'form': form})


@login_required(login_url='my-login')
def delete_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    return redirect('teacher-list')


@login_required(login_url='my-login')
def staff_list(request):
    staff = AdministrativeStaff.objects.all().order_by('role')
    context = {'staff':staff}
    return render(request, 'school/admin/staff-list.html', context)

@login_required(login_url='my-login')
def staff_id(request, staff_id):
    staff = get_object_or_404(AdministrativeStaff, id=staff_id)
    context = {
        'staff': staff
    }
    return render(request, 'school/admin/staff-id.html', context)


@login_required(login_url='my-login')
def support_staff(request):
    form = SupportForm()
    if request.method == "POST":
        form = SupportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Support staff added successfully.")
            return redirect('support-staff')
        else:
            messages.error(request, "There was an error submitting the form.")
    
    staffs = SupportStaff.objects.all()
    context = {
        'form': form,
        'staffs': staffs
    }
    return render(request, 'school/admin/support-staff.html', context)



@login_required(login_url='my-login')
def support_id(request, staff_id):
    staff = get_object_or_404(SupportStaff, id=staff_id)
    return render(request, 'school/admin/support-id.html', {'staff': staff})




@login_required(login_url='my-login')
def logoutUser(request):
    auth.logout(request)
    return redirect('my-login')



@login_required(login_url='my-login')
def global_search(request):
    query = request.GET.get('q')
    students = teachers = support_staff = admin_staff = []

    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) 
           
        )

        teachers = Teacher.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(teacher_id__icontains=query) |
            Q(email__icontains=query)
        )

        support_staff = SupportStaff.objects.filter(
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)|
            Q(role__icontains=query)
           
        )

        admin_staff = AdministrativeStaff.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(staff_id__icontains=query) |
            Q(role__icontains=query) |
            Q(email__icontains=query)
        )

    context = {
        'query': query,
        'students': students,
        'teachers': teachers,
        'support_staff': support_staff,
        'admin_staff': admin_staff
    }
    return render(request, 'school/search-results.html', context)
