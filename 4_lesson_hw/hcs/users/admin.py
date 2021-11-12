from django.contrib import admin
from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'personal_acc_hcs',
                    'personal_acc_landline_phone', 'personal_acc_distance_phone',
                    'created_at',)
    list_display_links = ('id', 'name', 'date_of_birth',)
    search_fields = ('name', 'date_of_birth',)
