# Generated by Django 5.1.4 on 2025-01-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='email_institucional',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='email_personal',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='email_institucional',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='email_personal',
            field=models.CharField(max_length=30),
        ),
    ]
