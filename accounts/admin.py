from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'get_date_of_birth', 'get_profile_image']

    fieldsets = (
        (('User'), {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_image'),
        }),
    )
    def get_date_of_birth(self, obj):
        return obj.profile.date_of_birth

    def get_profile_image(self, obj):
        return obj.profile.profile_image.url

    get_date_of_birth.short_description = 'Date of Birth'
    get_profile_image.short_description = 'Profile Image'

admin.site.register(CustomUser, CustomUserAdmin)
