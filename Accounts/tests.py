from django.test import TestCase
from django.test import Client
from . import models

class AtmTest(TestCase):
    def setUp(self) -> None:
        account1 = models.AccountInfo.objects.create(account_number='1234567890',balance=300)
        account2 = models.AccountInfo.objects.create(account_number='1111111111',balance=240)
        account3 = models.AccountInfo.objects.create(account_number='2222222222',balance=100)
        account4 = models.AccountInfo.objects.create(account_number='3333333333',balance=500)
        account5 = models.AccountInfo.objects.create(account_number='0123456789',balance=30)
        card1 = models.CardInfo.objects.create(card_number='1111222233334444',account_number=models.AccountInfo.objects.get(pk=account1.pk),pin="1234",name='a')
        card2 = models.CardInfo.objects.create(card_number='2222333344445555',account_number=models.AccountInfo.objects.get(pk=account2.pk),pin="1234",name='b')
        card3 = models.CardInfo.objects.create(card_number='3333444455556666',account_number=models.AccountInfo.objects.get(pk=account3.pk),pin="1234",name='c')
        card4 = models.CardInfo.objects.create(card_number='4444555566667777',account_number=models.AccountInfo.objects.get(pk=account4.pk),pin="1234",name='d')
        card5 = models.CardInfo.objects.create(card_number='5555666677778888',account_number=models.AccountInfo.objects.get(pk=account5.pk),pin="1234",name='e')
    def test_cash_deposit(self):
        c=Client()
        res=c.post('account:deposit')
        self.assertEqual(res.status_code,200)
        
