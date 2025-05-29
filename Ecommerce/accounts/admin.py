from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import CreateUserForm, ChangeUserForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = ChangeUserForm
    add_form = CreateUserForm

    list_display = ('phone', 'email', 'name', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields':('phone', 'email', 'password')}),
        ('Personal info', {'fields':('name',)}),
        ('Permissions', {'fields':('is_admin',)}),
    )

    add_fieldsets = (
        
        (None, {'classes': ('wide',),
                'fields':('phone', 'email', 'password1', 'password2')
                }),
    )

    search_fields = ('phone', 'email')
    ordering = ('phone',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User,UserAdmin)