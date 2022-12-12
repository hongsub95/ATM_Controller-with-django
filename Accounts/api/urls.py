from django.urls import path
from . import views

app_name="api_account"

urlpatterns = [
    path('account/',views.AccountListAPIView.as_view()),
    path('card/',views.CardListAPIView.as_view()),
]
