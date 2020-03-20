# Generated by Django 3.0.3 on 2020-03-09 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0005_auto_20200303_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='user',
        ),
        migrations.AddField(
            model_name='chart',
            name='day10',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day11',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day12',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day13',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day14',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day15',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day16',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day17',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day18',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day19',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day20',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day21',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day22',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day23',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day24',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day25',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day26',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day27',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day28',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day29',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day30',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day31',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day32',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day33',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day34',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day35',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day36',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day37',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day38',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day39',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day4',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day40',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=36.6, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day5',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day6',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day7',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day8',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='day9',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='comment',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='temperature',
            field=models.FloatField(blank=True, choices=[(36.0, ' 36.0 '), (36.05, ' 36.05 '), (36.1, ' 36.1 '), (36.15, ' 36.15 '), (36.2, ' 36.2 '), (36.25, ' 36.25 '), (36.3, ' 36.3 '), (36.35, ' 36.35 '), (36.4, ' 36.4 '), (36.45, ' 36.45 '), (36.5, ' 36.5 '), (36.55, ' 36.55 '), (36.6, ' 36.6 '), (36.65, ' 36.65 '), (36.7, ' 36.7 '), (36.75, ' 36.75 '), (36.8, ' 36.8 '), (36.85, ' 36.85 '), (36.9, ' 36.9 '), (36.95, ' 36.95 '), (37.0, ' 37.0 '), (37.05, ' 37.05 '), (37.1, ' 37.1 '), (37.15, ' 37.15 '), (37.2, ' 37.2 '), (37.25, ' 37.25 '), (37.3, ' 37.3 '), (37.35, ' 37.35 '), (37.4, ' 37.4 '), (37.45, ' 37.45 '), (37.5, ' 37.5 '), (37.55, ' 37.55 '), (37.6, ' 37.6 '), (37.65, ' 37.65 '), (37.7, ' 37.7 '), (37.75, ' 37.75 '), (37.8, ' 37.8 '), (37.85, ' 37.85 '), (37.9, ' 37.9 '), (37.95, ' 37.95 ')], default=None, null=True),
        ),
    ]