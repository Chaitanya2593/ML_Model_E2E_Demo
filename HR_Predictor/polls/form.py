from django.forms import ModelForm
from django import forms
from .models import dl_model, HR_pred
from django.forms import SelectDateWidget
import datetime
from django.utils import timezone

class FillForm(ModelForm):
    class Meta:
        model = dl_model
        exclude = ('Left', 'Dl model text')

class modelFillForm(forms.ModelForm):
    class Meta:
        model = HR_pred
        fields = ('__all__')

def past_years(ago):
    this_year = timezone.now().year
    return list(range(this_year-ago-1, this_year))

class RawFillForm(forms.Form):

    SELECT_COUNTRY = (
        ('Select','Select'),
        ('CH','CH'),
        ('IT', 'IT'),
        ('US', 'US'),
        ('AU', 'AU'),
        ('FR', 'FR'),
    )
    YEAR = (
        ('Select','Select'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
    )

    select_country = forms.CharField(label='Select Country', widget=forms.Select(choices=SELECT_COUNTRY), initial='Select')
    start_date = forms.DateField(label='Start Date', initial=datetime.date.today, widget=SelectDateWidget(years=past_years(1)))
    end_date = forms.DateField(label='End Date', initial=datetime.date.today, widget=SelectDateWidget())

