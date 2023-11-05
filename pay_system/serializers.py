from rest_framework import serializers
from .models import Reciever, Product


class RecieverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciever
        fields = ["id", "name", "wallet", "items", "signature"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["currency", "amount", "product_name", "product_description"]
