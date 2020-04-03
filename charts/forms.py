from django import forms
from .models import Chart
from django.utils.translation import gettext_lazy as _


class ChartForm(forms.Form):
    class Meta:
        model = Chart
        fields = '__all__'
        exclude = ['user']
        labels = {
            'start_date': _('Start date: (format YYYY-MM-DD)')
        }
        help_texts = {
            'start_date': _('End date: (format YYYY-MM-DD)')
        }
