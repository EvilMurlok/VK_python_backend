import re

# это можно было бы использовать для валидации пароля, но написал свой собственный,
# так как раздражает муть с "Общие пароли запрещены", а удобно вводить всем пароли Qwerty123
# from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from .models import Users


class DetailUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'username', 'first_name', 'last_name', 'date_of_birth',
                  'personal_acc_hcs', 'personal_acc_landline_phone', 'personal_acc_distance_phone']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'date_of_birth',
                  'personal_acc_hcs', 'personal_acc_landline_phone', 'personal_acc_distance_phone',
                  ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        try:
            Users.objects.get(email=email)
        except Users.DoesNotExist:
            return email
        raise serializers.ValidationError('That email is already taken, please do not lie us!!!')

    def validate_username(self, username):
        try:
            Users.objects.get(username=username)
        except Users.DoesNotExist:
            return username
        raise serializers.ValidationError('That username is already taken, please select another!')

    def validate_password(self, password):
        if password.lower() == password:
            raise serializers.ValidationError('Password should contains at least one capital letter!')
        elif password.isdigit():
            raise serializers.ValidationError('Password must not be numeric!')
        elif len(password) < 8:
            raise serializers.ValidationError('Password must not be shorter then 8 symbols')
        else:
            return password

    def validate_first_name(self, first_name):
        if re.match(r'[A-Z][a-z]', first_name):
            return first_name
        raise serializers.ValidationError('The entered first name must consists of only letters!')

    def validate_last_name(self, last_name):
        if re.match(r'[A-Z][a-z]', last_name):
            return last_name
        raise serializers.ValidationError('The entered last name must consists of only letters!')

    def validate_personal_acc_distance_phone(self, personal_acc_distance_phone):
        if personal_acc_distance_phone < 0:
            raise serializers.ValidationError('Personal account for phone payments cannot be less than zero!')
        return personal_acc_distance_phone

    def validate_personal_acc_hcs(self, personal_acc_hcs):
        if personal_acc_hcs < 0:
            raise serializers.ValidationError('Personal account for hcs payments cannot be less than zero!')
        return personal_acc_hcs

    def validate_personal_acc_landline_phone(self, personal_acc_landline_phone):
        if personal_acc_landline_phone < 0:
            raise serializers.ValidationError('Personal account for phone payments cannot be less than zero!')
        return personal_acc_landline_phone


class UpdateUserUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'last_name']

    def validate_last_name(self, last_name):
        if re.match(r'[A-Z][a-z]', last_name):
            return last_name
        raise serializers.ValidationError('The entered last name must consists of only letters!')


class UpdateUserUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', ]


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(required=True)

    class Meta:
        model = Users
        fields = ['old_password', 'new_password', ]

    def validate_new_password(self, new_password):
        if new_password.lower() == new_password:
            raise serializers.ValidationError('Password should contains at least one capital letter!')
        elif new_password.isdigit():
            raise serializers.ValidationError('Password must not be numeric!')
        elif len(new_password) < 8:
            raise serializers.ValidationError('Password must not be shorter then 8 symbols')
        else:
            return new_password
