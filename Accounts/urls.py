from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('card-insert/',views.InsertCardView,name="InsertCard"),
    path('card-remove/',views.RemoveCardView,name='RemoveCard'),
    path('transaction-history/',views.transaction_history,name="transaction-history"),
    path('balance/',views.BalanceView,name="balance"),
    path('deposit/',views.DepositView,name='deposit'),
    path('withdraw/',views.WithdrawView,name='withdraw'),
]