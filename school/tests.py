{% extends 'school/base.html' %}
{% load crispy_forms_tags %}
{% load static tailwind_tags %}
{% load widget_tweaks %}
{% load static %}

{% block body %}
<div class="page-wrapper bg-gray-100">
    <div class="content container-fluid">
        <div class="page-header">
            <div class="row align-items-center">
                <div class="col">
                    <h3 class="page-title">Teacher Information</h3>
                    <ul class="breadcrumb">
                        <li class="breadcrumb-item"><a href="{% url 'admin-dashboard' %}">Dashboard</a></li>
                        <li class="breadcrumb-item active">Teacher Info</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <!-- ID Card Layout -->
        <div class=" bg-gray-100 ">
            <div class="w-[600px] h-[250px]  bg-white shadow-xl rounded-xl border-4 border-blue-600 overflow-hidden">
    
                <!-- Full-width Header -->
                <div class="bg-blue-100 px-4 py-2 flex items-center gap-3 rounded border-b border-blue-300">
                    <img src="{% static 'assets/images/logo1.jpg' %}" alt="Logo" class="h-10 w-10">
                    <div>
                        <h2 class="font-weight-600 text-blue-800 text-sm">Alyaqeen Academy ID card</h2>
                     
                    </div>
                </div>

                <!-- Body: Image + Info -->
                <div class="flex h-full">
                    <!-- Left: Profile Picture -->
                    <div class="w-1/3 bg-gray-100 flex items-center justify-center border-r border-gray-300 p-3">
                        <img src="{% if teacher.profile_picture %}{{ teacher.profile_picture.url }}{% else %}https://via.placeholder.com/150{% endif %}" 
                            alt="Profile" class="w-28 h-36 object-cover border border-gray-400 shadow-md">
                    </div>

                    <!-- Right: Info -->
                    <div class="w-2/3 p-4 flex flex-col justify-between">
                        <div class="text-sm text-gray-800 space-y-1">
                            <p><strong>Name:</strong> {{ teacher.first_name|title }} {{ teacher.last_name|title }}</p>
                            <p><strong>Gender:</strong> {{ teacher.gender }}</p>
                            <p><strong>Section:</strong> {{ teacher.section }}</p>
                            <p><strong>Staff ID:</strong> {{ teacher.teacher_id }}</p>
                        </div>

                        <div class="text-[10px] text-gray-600 mt-2 border-t pt-1">
                            <p>Authorized by: School Management</p>
                            <p>Valid for: {{ academic_session.name }}</p>
                        </div>
                    </div>
                </div>

            </div>

        </div>
        
    </div>
</div>

<script src="{% static 'assets/js/jquery-3.6.0.min.js' %}"></script>
<script src="{% static 'assets/js/popper.min.js' %}"></script>
<script src="{% static 'assets/plugins/bootstrap/js/bootstrap.min.js' %}"></script>
<script src="{% static 'assets/plugins/slimscroll/jquery.slimscroll.min.js' %}"></script>
<script src="{% static 'assets/js/script.js' %}"></script>
{% endblock %}
