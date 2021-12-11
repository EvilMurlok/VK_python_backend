import re
from django import forms
from .models import Users
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'personal_acc_hcs',
                  'personal_acc_landline_phone', 'personal_acc_distance_phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': MyDateInput({'class': 'form-control'}),
            'personal_acc_hcs': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_acc_landline_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_acc_distance_phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Users.objects.get(username=username)
        except Users.DoesNotExist:
            return username
        raise forms.ValidationError('That username is already taken, please select another.')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if re.match(r'[A-Z][a-z]', first_name):
            return first_name
        raise ValidationError('The entered first name must consists of only letters!')

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if re.match(r'[A-Z][a-z]', last_name):
            return last_name
        raise ValidationError('The entered last name must consists of only letters!')

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


class UserRegistrationForm(forms.ModelForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'password', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': MyDateInput({'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Users.objects.get(username=username)
        except Users.DoesNotExist:
            return username
        raise forms.ValidationError('That username is already taken, please select another.')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if re.match(r'[A-Z][a-z]', first_name):
            return first_name
        raise ValidationError('The entered first name must starts with a big letter and consists of only letters!')

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if re.match(r'[A-Z][a-z]', last_name):
            return last_name
        raise ValidationError('The entered last name must starts with a big letter and consists of only letters!')

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError('The length of thr password should be more 7 symbols!')
        elif password.lower() == password:
            raise ValidationError('The password should contains at least one big letter!')
        elif password.isdigit():
            raise ValidationError('The password should not be a number!')
        else:
            return password

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return self.cleaned_data['password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

