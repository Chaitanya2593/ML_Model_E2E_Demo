from django.db import models
from django import forms

class dl_model(models.Model):
    dl_model_text = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.dl_model_text

class HR_pred(models.Model):
    file_upload = models.FileField(upload_to='uploads/')

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
    analysis_year = forms.CharField(label='Analysis Year', widget=forms.Select(choices=YEAR), initial='Select')


