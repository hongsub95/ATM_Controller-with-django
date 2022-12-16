from django.urls import path
from . import views

app_name="api_account"

urlpatterns = [
    path('account/',views.AccountListCreateAPIView.as_view()),
    path('card/',views.CardListCreateAPIView.as_view()),
]
