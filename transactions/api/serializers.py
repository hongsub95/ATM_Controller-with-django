from rest_framework import serializers
from transactions import models as transaction_models

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction_models.transaction
        fields="__all__"