# Generated by Django 3.0.3 on 2020-04-03 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='born_date',
        ),
    ]
