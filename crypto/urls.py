from django.urls import path
from .views import *

urlpatterns = [
    path('<str:ticker>/', detail_coin, name="detail_coin"),
    path('', list_coins, name="list_coins"),
    path('coins/', CoinView.as_view(), name='coin_view'),
]
