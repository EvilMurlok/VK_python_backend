from django.contrib import admin
from .models import Users, Address, Receipt
from django.contrib.auth.admin import UserAdmin


@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'date_of_birth', 'personal_acc_hcs',
                    'personal_acc_landline_phone', 'personal_acc_distance_phone',
                    'created_at', 'is_staff', 'address', 'flat_number',)
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'date_of_birth',)
    search_fields = ('first_name', 'last_name', 'date_of_birth',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('Fill all fields', {'fields': ('username', 'email', 'password', 'first_name', 'last_name',
                                        'date_of_birth', 'personal_acc_hcs',
                                        'personal_acc_landline_phone', 'personal_acc_distance_phone', 'address',
                                        'flat_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ('Fill all fields', {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2', 'is_staff', 'is_active',
                'first_name', 'last_name',
                'date_of_birth', 'personal_acc_hcs',
                'personal_acc_landline_phone', 'personal_acc_distance_phone', 'flat_number',
            )}
         ),
    )
    ordering = ['-personal_acc_hcs']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'street', 'house', 'housing', )
    list_display_links = ('id', 'city_name', 'street', )
    search_fields = ('city_name', 'street', )


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount_units', 'units', 'amount_money', 'service', 'period_of_receipt', 'users',)
    list_display_links = ('id', 'amount_units',  'units', 'amount_money', 'service',)
    search_fields = ('period_of_receipt', 'service', 'users',)
