from django.contrib import admin

from User.models import User


@admin.register(User)
class UserInformation(admin.ModelAdmin):
    list_display = (
        'nickname',
        'avatar',
    )


