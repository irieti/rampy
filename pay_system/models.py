from django.db import models


class Reciever(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    wallet = models.CharField(max_length=100)
    signature = models.CharField(max_length=1000)
    items = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.id}: {self.name}, {self.wallet}"


class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True)
    product_description = models.CharField(max_length=500, blank=True)
    currency = models.CharField(max_length=100)
    amount = models.FloatField()
    reciever = models.ForeignKey(Reciever, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name} of {self.reciever}: {self.amount} {self.currency}"
