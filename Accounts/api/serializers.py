from rest_framework import serializers
from Accounts import models as account_models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.AccountInfo
        fields = ["account_number","balance",]

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.CardInfo
        fields = ["name","account_number","card_number","pin","phone_number",]