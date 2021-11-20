from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin


@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'date_of_birth', 'personal_acc_hcs',
                    'personal_acc_landline_phone', 'personal_acc_distance_phone',
                    'created_at',)
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'date_of_birth',)
    search_fields = ('first_name', 'last_name', 'date_of_birth',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('Fill all fields', {'fields': ('username', 'email', 'password', 'first_name', 'last_name',
                                 'date_of_birth', 'personal_acc_hcs',
                                 'personal_acc_landline_phone', 'personal_acc_distance_phone',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ('Fill all fields', {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2', 'is_staff', 'is_active',
                'first_name', 'last_name',
                'date_of_birth', 'personal_acc_hcs',
                'personal_acc_landline_phone', 'personal_acc_distance_phone',
            )}
         ),
    )
    ordering = ['-personal_acc_hcs']
