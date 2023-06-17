from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm


User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """This class is for User Admin panel."""
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = [
        'username',
        'email',
        'is_staff',
        'last_login',
        'date_joined'
    ]
    list_filter = [
        'is_active',
        'is_staff',
        'is_superuser'
    ]
    search_fields = [
        'username__icontains',
        'email__icontains'
    ]
    ordering = [
        '-is_superuser',
        '-is_staff',
        '-last_login'
    ]
    list_per_page = 10
