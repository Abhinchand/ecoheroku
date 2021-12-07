from rest_framework import serializers
from .models import *

class AmountSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = amount
        fields = '__all__'