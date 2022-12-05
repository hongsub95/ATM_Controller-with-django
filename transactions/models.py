from django.db import models

class transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True,unique=True)
    TRANSACTION_TYPE = (("balance","balance"),("withdraw","withdraw"),("deposit","deposit"),("transfer"),("transfer"))
    transaction_type = models.CharField(max_length=20,choices=TRANSACTION_TYPE,default="balance")
    card_number = models.ForeignKey("Accounts.CardInfo",to_field="card_number",on_delete=models.DO_NOTHING)
    response_code = models.CharField(max_length=3)
    
