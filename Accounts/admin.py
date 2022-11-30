from django.contrib import admin
from . import models 


@admin.register(models.CardInfo)
class CardAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields":("name","account_number","card_number","pin","phone_number",),
        }),
    )
    list_display = ("name","card_number","account_number")

@admin.register(models.AccountInfo)
class AccountAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "account_number","balance",
            ),
        }),
    )
    list_display = ("account_number","balance")