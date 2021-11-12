import re
from django import forms
from .models import Users
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'date_of_birth', 'personal_acc_hcs',
                  'personal_acc_landline_phone', 'personal_acc_distance_phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': MyDateInput({ 'class': 'form-control' }),
            'personal_acc_hcs': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_acc_landline_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_acc_distance_phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'[A-Z][a-z]+\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?', name):
            return name
        raise ValidationError('The entered name is not in the correct format!')

    def clean_personal_acc_distance_phone(self):
        personal_acc_distance_phone = self.cleaned_data['personal_acc_distance_phone']
        if personal_acc_distance_phone < 0:
            raise ValidationError('Personal account for phone payments cannot be less than zero!')
        return personal_acc_distance_phone

    def clean_personal_acc_hcs(self):
        personal_acc_hcs = self.cleaned_data['personal_acc_hcs']
        if personal_acc_hcs < 0:
            raise ValidationError('Personal account for hcs payments cannot be less than zero!')
        return personal_acc_hcs

    def clean_personal_acc_landline_phone(self):
        personal_acc_landline_phone = self.cleaned_data['personal_acc_landline_phone']
        if personal_acc_landline_phone < 0:
            raise ValidationError('Personal account for phone payments cannot be less than zero!')
        return personal_acc_landline_phone
