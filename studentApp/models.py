from django.db import models
from school.models import*


class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(unique=True, max_length=11)
    relationship = models.CharField(max_length=30)  
    address = models.CharField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.relationship})"
    
Gender = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class Student(models.Model):
    guardian = models.ForeignKey(Guardian, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True, blank=True)

    gender = models.CharField(max_length=10, choices=Gender)
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=20)
    date_join = models.DateField()
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(upload_to='students/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.first_name}  {self.last_name} ( Parent : ---> {self.guardian.first_name} )"
    