from django.urls import path
from . import views

app_name="api_administrator"

urlpatterns = [
    path('account/',views.AccountListCreateAPIView.as_view(),name="account-api"),
    path('account/',views.AccountRetrieveUpdateDestroyAPIView.as_view(),name="account-api"),
    path('card/',views.CardListCreateAPIView.as_view(),name="card-api"),
    path('card/',views.CardRetrieveUpdateDestroyAPIView.as_view(),name="card-api"),
]
