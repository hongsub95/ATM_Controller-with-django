from django.shortcuts import render
from . import models as transaction_models
from Accounts import models as accounts_models

#It knows transaction-history

def renderpage(renderdata):
    if not renderdata['request']:
        return 'No request provided'
    if not renderdata['path']:
        return 'No template path provided'
    if not renderdata['context']:
        return render(renderdata['request'],renderdata['path'])
    return render(renderdata['request'],renderdata['path'],renderdata['context'])

def getCardByNumber(CardNumber):
    try:
        card = accounts_models.CardInfo.objects.get(card_number=CardNumber)
    except:
        return False
    return card

def getTransactionCard(CardNumber):
    try:
        transactions = transaction_models.transaction.objects.filter(card_number=CardNumber)
    except:
        return False
    if len(transactions) == 0: # if transactions does not exist , return False
        return False
    return transactions

def getMessageData(data,msg):
    data['message'] = msg
    return 
        