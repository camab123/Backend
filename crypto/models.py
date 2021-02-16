from django.db import models

# Create your models here.
class Coin(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = price = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name
    
    def serialize(self):
        return {
            'ticker': self.ticker,
            'name': self.name,
            'price': self.price,
        }