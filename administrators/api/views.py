from rest_framework import generics
from Accounts import models as account_models
from . import serializers  as account_serializer

class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = account_models.AccountInfo.objects.all()
    def get_serializer_class(self):
        if self.request.method == "GET":
            return account_serializer.AccountSerializer
        else:
            return account_serializer.AccountCreateSerializer
    

class CardListCreateAPIView(generics.ListCreateAPIView):
    queryset = account_models.CardInfo.objects.all()
    def get_serializer_class(self):
        if self.request.method == "GET":
            return account_serializer.CardSerializer
        else:
            return account_serializer.CardCreateSerializer

        
        
    