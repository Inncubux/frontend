# Generated by Django 5.1.4 on 2025-01-08 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email_institucional', models.EmailField(max_length=254)),
                ('email_personal', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('horas', models.IntegerField()),
                ('seccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email_institucional', models.EmailField(max_length=254)),
                ('email_personal', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mentoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.alumno')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.asignatura')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.mentor')),
            ],
        ),
    ]
