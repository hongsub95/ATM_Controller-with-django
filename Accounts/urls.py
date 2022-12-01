from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('card-insert/',views.InsertCardView,name="InsertCard"),
    path('card-remove/',views.RemoveCardView,name='RemoveCard'),
    path('<int:pk>/transaction/',views.TransactionView,name="transaction"),
    path('<int:pk>/balance/',views.BalanceView,name="balance"),
    path('<int:pk>/deposit/',views.DepositView,name='deposit'),
    path('<int:pk>/withdraw/',views.WithdrawView,name='withdraw'),
]