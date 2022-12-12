from django.urls import path
from . import views

app_name = "api_transaction"

urlpatterns = [
    path('',views.TransactionListAPIView.as_view())
]
