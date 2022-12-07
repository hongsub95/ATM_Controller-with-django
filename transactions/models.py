from django.db import models
from django.utils import timezone

class transaction(models.Model):
    STATUS_CHOICES = (
        ('canceled', 'Canceled'), #취소
        ('pending', 'Pending'),  #대기중
        ('complete', 'Complete') #완료
    )
    TRANSACTION_TYPE = (
        ("balance","balance"), # 잔액조회
        ("withdraw","withdraw"), # 인출
        ("deposit","deposit"), # 입금
        ("transfer","transfer") # 송금
    )
    transaction_id = models.AutoField(primary_key=True,unique=True)
    transaction_type = models.CharField(max_length=20,choices=TRANSACTION_TYPE,default="balance")
    card_number = models.ForeignKey("Accounts.CardInfo",to_field="card_number",on_delete=models.DO_NOTHING)
    response_code = models.CharField(max_length=3)
    date = models.DateField(default = timezone.now)
    status = models.CharField(
        max_length = 12, 
        choices = STATUS_CHOICES, 
        default = 'pending'
    )
