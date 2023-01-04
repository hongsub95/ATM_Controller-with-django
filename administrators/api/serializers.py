from rest_framework import serializers
from Accounts import models as account_models
from transactions import services

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.AccountInfo
        fields = ["account_number","balance",]
        depth = 1

class CardSerializer(serializers.ModelSerializer):
    account_number = AccountSerializer()
    class Meta:
        model = account_models.CardInfo
        fields = ["name","account_number","card_number","pin","phone_number",]

class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.AccountInfo
        fields = ["account_number","balance",]

class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.AccountInfo
        fields = ["account_number","balance",]

    def create(self,validate_data):
        AccNum = services.CreateAccountNum()
        account = account_models.AccountInfo.objects.create(account_number=AccNum,balance=0)
        return account
        
class CardCreateSerializer(serializers.ModelSerializer):
    account_number = AccountSerializer()
    class Meta:
        model = account_models.CardInfo
        fields = ["name","account_number","card_number","pin","phone_number",]
        extra_kwargs = {
            "account_number":{"write_only":True}
        }
    def create(self,validate_data):
        acc_number =validate_data.pop("account_number")
        name = validate_data.pop("name")
        pin = validate_data.pop("pin")
        phone_number=validate_data.pop("phone_number")
        CardNum = services.CreateCardNum()
        if acc_number["account_number"] == '0':
            AccNum = services.CreateAccountNum()
            account = account_models.AccountInfo.objects.create(account_number=AccNum,balance=0)
            account.save()
            card = account_models.CardInfo(card_number=CardNum,name=name,pin=pin,phone_number=phone_number)
            card.account_number=account
            card.save()
        else:
            try:
                account = account_models.AccountInfo.objects.get(account_number=acc_number["account_number"])
                print(account)
                card = account_models.CardInfo(card_number=CardNum,name=name,pin=pin,phone_number=phone_number)
                card.account_number = account
                card.save()
            except:
                raise serializers.ValidationError(
                {'error': 'Account Number does not exist'}
                ) 
        return card