from django.db import models

class AccountInfo(models.Model):
    account_number = models.CharField(
        primary_key=True,
        max_length = 10,
        unique = True,
        verbose_name="계좌번호",
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
        verbose_name="카드번호",
    )
    pin = models.CharField(
        max_length = 4,
        verbose_name="핀번호"
    )

    phone_number = models.CharField(max_length=11, blank=True,verbose_name="전화번호")
