from rest_framework import generics
from Accounts import models as account_models
from . import serializers  as account_serializer

class AccountListAPIView(generics.ListAPIView):
    queryset = account_models.AccountInfo.objects.all()
    serializer_class = account_serializer.AccountSerializer

class CardListAPIView(generics.ListAPIView):
    queryset = account_models.CardInfo.objects.all()
    serializer_class = account_serializer.CardSerializer
