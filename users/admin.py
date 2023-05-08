from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = CustomUser
    # set available filter fields in admin panel
    search_fields = ('firstname', 'lastname', 'username')
    list_filter = ('is_active', 'is_staff')
    ordering = ('username',)
    list_display = ('username', 'firstname', 'lastname',
                    'is_active', 'is_staff')
    # Set how the fields are sectioned in the users area of the admin panel
    fieldsets = (
        (None, {'fields': ('email', 'username', 'firstname', 'lastname',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('profilepic',)}),
    )
    # fields available when adding a new user from the admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'firstname', 'lastname',
                       'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)
