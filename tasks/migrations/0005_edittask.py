# Generated by Django 5.0.2 on 2024-02-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_employeeid_tasks_empname'),
    ]

    operations = [
        migrations.CreateModel(
            name='edittask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskID', models.TextField()),
            ],
        ),
    ]
