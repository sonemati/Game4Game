from django.contrib import admin
from .models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class UserProfileInline(admin.StackedInline):
    model = UserProfileInfo
    can_delete = False


class AccountsUserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)
