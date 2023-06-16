# Generated by Django 4.2.2 on 2023-06-15 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('credits', models.PositiveSmallIntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=60)),
                ('full_name', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=12)),
                ('birth_day', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('course_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy_management.course')),
                ('student_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy_management.student')),
            ],
        ),
    ]