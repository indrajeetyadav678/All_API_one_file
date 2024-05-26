from rest_framework import serializers
from .models import*

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'
        # fields=['id', 'Image', 'Prod_Name', 'Prod_price', "Prod_offer", 'Prod_decription', 'Prod_use']
