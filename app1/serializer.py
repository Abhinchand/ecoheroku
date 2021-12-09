from rest_framework import serializers
from .models import *
from phonenumber_field.modelfields import PhoneNumberField


class AmountSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = amount
        fields = '__all__'


class UserCreation(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    phone_numbers = serializers.IntegerField()
    images = serializers.ImageField()
    district = serializers.CharField(max_length=50)
    pincode = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = '__all__'


class loginseialize(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
