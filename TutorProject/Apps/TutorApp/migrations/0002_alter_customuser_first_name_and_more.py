# Generated by Django 4.2.6 on 2023-10-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
