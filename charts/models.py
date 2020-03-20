import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from io import BytesIO
import base64
from datetime import timedelta
from django.db import models
from django.utils import timezone  # for timezone.now
from django.contrib.auth.models import User  # authorize user (seperate table)
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)  # date when object was created, cannot update
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # foreignkey bo z drugiej bazy(klasy), delete post if user is deleted

    def __str__(self):  # co ma zwrócić jeśli ktoś się odwowła do obiektu
        return (self.title)


temp_choice = (
    (36.0, ' 36.00 '), (36.05, ' 36.05 '), (36.1, ' 36.10 '), (36.15, ' 36.15 '), (36.2, ' 36.20 '), (36.25, ' 36.25 '),
    (36.3, ' 36.30 '), (36.35, ' 36.35 '), (36.4, ' 36.40 '), (36.45, ' 36.45 '), (36.5, ' 36.50 '), (36.55, ' 36.55 '),
    (36.6, ' 36.60 '), (36.65, ' 36.65 '), (36.7, ' 36.70 '), (36.75, ' 36.75 '), (36.8, ' 36.80 '), (36.85, ' 36.85 '),
    (36.9, ' 36.90 '), (36.95, ' 36.95 '), (37.0, ' 37.00 '), (37.05, ' 37.05 '), (37.1, ' 37.10 '), (37.15, ' 37.15 '),
    (37.2, ' 37.20 '), (37.25, ' 37.25 '), (37.3, ' 37.30 '), (37.35, ' 37.35 '), (37.4, ' 37.40 '), (37.45, ' 37.45 '),
    (37.5, ' 37.50 '), (37.55, ' 37.55 '), (37.6, ' 37.60 '), (37.65, ' 37.65 '), (37.7, ' 37.70 '), (37.75, ' 37.75 '),
)

class Day(models.Model):
    date = models.DateField(default=timezone.now, blank=True, null=True)
    temperature = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    bleeding = models.BooleanField(default=False)
    spotting = models.BooleanField(default=False)

# class DayForm(ModelForm):
#     class Meta:
#         day = Day
#         fields = ['date', 'temperature', 'bleeding', 'spotting']

class Chart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cycle = models.IntegerField()
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True, null=True, name='End date: (format YYYY-MM-DD)')
    comment = models.CharField(max_length=150, blank=True)
    day1 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day2 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day3 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day4 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day5 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day6 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day7 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day8 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day9 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day10 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day11 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day12 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day13 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day14 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day15 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day16 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day17 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day18 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day19 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day20 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day21 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day22 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day23 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day24 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day25 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day26 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day27 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day28 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day29 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day30 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day31 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day32 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day33 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day34 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day35 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day36 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day37 = models.FloatField(choices=temp_choice, default=None, blank=True, null=True)
    day38 = models.FloatField(choices=temp_choice, blank=True, null=True)
    day39 = models.FloatField(choices=temp_choice, blank=True, null=True)
    day40 = models.FloatField(choices=temp_choice, blank=True, null=True)

    def __str__(self):
        return (self.user, self.cycle)

    def get_absolute_url(self):         # location for a specific chart after chart is created
        return reverse('chart-detail', kwargs={'pk': self.pk})  #

    def get_days(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields[6:]]

    def enddate(self):
        enddate = self.start_date + timedelta(days=28)
        return str(enddate)

    def show_chart(self):
        plt.clf()
        days  = []
        temps = []
        i = 0
        for day,temp in self.get_days():
            i= i + 1
            if temp is None:
                continue
            days.append(i)
            temps.append(temp)
        plt.plot(days,temps, marker='o')
        plt.axis([1, 40, 36, 37.40])
        plt.xlabel('Days')
        plt.ylabel('Temperature')
        plt.grid('True')
        name = 'media/temp_charts/' + str(self.user) +str(self.cycle) + '.png'
        plt.savefig(name, format='png', width='')
        return '../../../' + name

# class Day(Chart):
#     date = models.DateField(default=timezone.now, blank=False, null=True)
#     temperature = models.FloatField(choices=temp_choice, default=36.6)
#     bleeding = models.BooleanField(default=False)
#     spotting = models.BooleanField(default=False)
# user = models.ForeignKey(User, on_delete=models.CASCADE)
#
# def __str__(self):
#     return (self.user, self.date, self.temperature)
#
# def get_absolute_url(self):
#     return reverse('chart-detail', kwargs={'pk': self.pk})
