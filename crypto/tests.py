from django.test import TestCase
from .models import *
# Create your tests here.

class CoinModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coin.objects.create(name='CamCoin', ticker="CAMUSDT", price=20)

    def test_name_content(self):
        coin = Coin.objects.get(id=1)
        expected_object_name = f'{coin.name}'
        self.assertEquals(expected_object_name, 'CamCoin')
    
    def test_ticker_content(self):
        coin = Coin.objects.get(id=1)
        expected_object_ticker = f'{coin.ticker}'
        self.assertEquals(expected_object_ticker, 'CAMUSDT')
    def test_price_content(self):
        coin = Coin.objects.get(id=1)
        expected_object_price = coin.price
        self.assertEquals(expected_object_price, 20)