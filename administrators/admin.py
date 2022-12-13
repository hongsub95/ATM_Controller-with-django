from django.contrib import admin
from . import models

@admin.register(models.AdminUser)
class AccountAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "username","password",
            ),
        }),
    )
    list_display = ("username",)
