from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    name = models.CharField(max_length=10, default="SY")
    full_name = models.CharField(max_length=50, default="Tech Company")
    description = models.TextField(default="A promising tech company")
    ltp = models.FloatField(default=100.0000)
    # generation data
    variance_lower_bound = models.FloatField(default=0.99)
    variance_upper_bound = models.FloatField(default=1.01)

    def __str__(self):
        return self.name


class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.FloatField(default=100.00)
    time = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    units = models.IntegerField()
    price_each = models.FloatField()
    choices = (
        ("sell", "sell"),
        ("buy", "buy"),
    )
    transaction = models.CharField(max_length=5, choices=choices)


class Portfolio(models.Model):
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class AccountValue(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    value = models.FloatField(default=10000.00)
    holdings_value = models.FloatField(default=0.0)
