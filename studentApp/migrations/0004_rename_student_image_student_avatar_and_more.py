# Generated by Django 5.2.2 on 2025-06-18 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0003_remove_student_mobile_number_student_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_image',
            new_name='avatar',
        ),
        migrations.RemoveField(
            model_name='student',
            name='admission_number',
        ),
    ]
