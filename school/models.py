from django.db import models
from django.core.exceptions import ValidationError
import uuid

#Academic Sesstion eg 2024/2025
class AcademicSession(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# Academic Term eg first | second |third term
class Term(models.Model):
    TERM =(
        ('1st term', 'First Term'),
        ('2nd term', 'Second Term'),
        ('3rd term', 'Third Term'),
    )
    name = models.CharField(max_length=10, choices=TERM, unique=True)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# section sub_school
class Section(models.Model):
    SECTION_CHOICES = (
        ('Nursery', 'Nursery'),
        ('Primary', 'Primary Section'),
        ('Junior', 'Junior Section'),
        ('Senior', 'Senior Section'),
    )
    name = models.CharField(max_length=10, choices=SECTION_CHOICES, unique=True)

    def __str__(self):
        return self.name

# sub_school subject
class Subject(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    class Meta:
        ordering = ['section', 'name']

    def __str__(self):
        return f"{self.name}"
    


# Teachers Info
class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    QUALIFICATION_CHOICES = (
        ('BSC', 'Bachelor Degree'),
        ('HND', 'Higher National Diploma'),
        ('ND', 'National Diploma'),
    )

    teacher_id = models.CharField(max_length=12, unique=True, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    

    


    def save(self, *args, **kwargs):
        if not self.teacher_id:
            self.teacher_id = f"AYQ-TCH-{str(uuid.uuid4().int)[-4:]}"
        super().save(*args, **kwargs)  
    
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

# class 
class SchoolClass(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)  # e.g. "JS1", "SS2", "Nursery 2"
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher_of')

    class Meta:
        unique_together = ('section', 'name')
        ordering = ['section', 'name']

    def __str__(self):
        return f"{self.name} ({self.section.name})"

