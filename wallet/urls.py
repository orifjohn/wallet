from django.urls import path
from .views import WalletView, TransactionView


urlpatterns = [
    path('wallet/<str:wallet_id>/', WalletView.as_view()),
    path('transaction/', TransactionView.as_view()),
]
