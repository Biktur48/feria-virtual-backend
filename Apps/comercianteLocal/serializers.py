from dataclasses import fields
from rest_framework import serializers
from .models import *

class BuyingOfferSerializer(serializers.ModelSerializer): 
    class Meta:
        model = BuyingOffer
        fields = ("__all__")
        