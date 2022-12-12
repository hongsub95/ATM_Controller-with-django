from rest_framework import generics
from transactions import models as transaction_models
from transactions.api import serializers as transaction_serializers


class TransactionListAPIView(generics.ListAPIView):
    queryset = transaction_models.transaction.objects.all()
    serializer_class =  transaction_serializers.TransactionSerializer