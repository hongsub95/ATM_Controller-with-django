from django.db import models
from django.core.validators import RegexValidator


class AccountInfo(models.Model):
    account_number = models.CharField(
        primary_key=True,
        max_length = 10,
        unique = True
    )
    balance = models.BigIntegerField(verbose_name="잔액")


#카드정보
class CardInfo(models.Model): 
    name = models.CharField(
        max_length = 35,verbose_name="이름"
    )
    account_number = models.ForeignKey(
        AccountInfo,
        on_delete=models.DO_NOTHING,  
        default = None,
        verbose_name="계좌번호"
    )
    card_number = models.CharField(
        primary_key=True,
        max_length = 16,
        unique=True,
        verbose_name="카드번호"
    )
    pin = models.CharField(
        max_length = 4,
        verbose_name="핀번호"
    )

    phone_number = models.CharField(validators=[RegexValidator(r'010-?[1-9]\d{3}-?\d{4}$')], max_length=13, blank=True,verbose_name="전화번호")
