# Generated by Django 5.0.2 on 2024-02-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='emprole',
            field=models.TextField(default='blank', max_length=500),
        ),
    ]
