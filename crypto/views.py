from django.shortcuts import render
from rest_framework import generics
from .models import Coin
from .serializers import *
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.


@api_view(['GET'])
def list_coins(request):
    qs = Coin.objects.all()
    serialized = [e.serialize() for e in qs]
    return Response(serialized, status=200)

@api_view(['GET'])
def detail_coin(request, ticker):
    ticker = ticker.upper()
    qs = Coin.objects.filter(ticker= ticker)
    serialized = [e.serialize() for e in qs]
    return Response(serialized, status=200)

class CoinView(APIView):
    def get(self, request):
        qs = Coin.objects.all()
        serialized = [e.serialize() for e in qs]
        return Response(serialized, status=200)
