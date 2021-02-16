import numpy as np
import pandas as pd
from binance.client import Client
import requests, json
from datetime import datetime, timedelta
from crypto.models import *

def get_client():
    api_key = 'c1yDVEPh8NrLVp2QBXQ8z5eOw1OP7f5F4DY6glf26xMzPQKTYEFfdEvdqMcmbEY7'
    api_secret = 'l1GPfLdXyLTaDOSZlJg2HlaHkCYH5DWt6oFRM8T6UyD4VCF3aqlJkm7VBUZen3d1'
    client = Client(api_key, api_secret)
    return client

def select_coins():
    coins = [
            ["BTCUSDT", "Bitcoin"],
            ["ETHUSDT", "Ethereum"],
            ["ADAUSDT", "Cardano"],
            ["DOGEUSDT", "Dogecoin"],
            ["BCHUSDT", "BTC Cash"],
            ["LTCUSDT", "Litecoin"],
            ['VETUSDT', "VeChain"],
            ['ATOMUSDT', "Cosmos"],
            ['VTHOUSDT', 'VeThor']
            ]
    coins_df = pd.DataFrame(coins, columns = ['symbol', 'Name'])
    return coins_df

def init_coins():
    Coin.objects.all().delete()
    client = get_client()
    coins_df = select_coins()
    tickers = client.get_ticker()
    ticker_df = pd.DataFrame(tickers)
    ticker_df = ticker_df.set_index('symbol')
    ticker_df = ticker_df.drop(['firstId', 'lastId', 'count'], axis = 1)
    ticker_df = ticker_df.reset_index(inplace=False, drop = False)
    coins_df = coins_df.merge(ticker_df, how='inner', on='symbol')
    
    for index, row in coins_df.iterrows():
        Ticker = row['symbol']
        Name = row['Name']
        coin_data = Coin(ticker = Ticker, name = Name)
        coin_data.save()
    

from django.core.management.base import BaseCommand
class Command(BaseCommand):

    help = 'data_collection'

    def add_arguments(self, parser):
        parser.add_argument('--selector', type=str, help='whichCommand')

    def handle(self, *args, **kwargs):
        selector = kwargs['selector']

        if selector == 'init_coins':
            init_coins()