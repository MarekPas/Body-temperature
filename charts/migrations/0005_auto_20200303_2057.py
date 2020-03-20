# Generated by Django 3.0.3 on 2020-03-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_auto_20200303_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='comment',
            field=models.CharField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], max_length=150),
        ),
        migrations.AlterField(
            model_name='day',
            name='temperature',
            field=models.FloatField(choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.05),
        ),
    ]