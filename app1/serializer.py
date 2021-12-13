from rest_framework import serializers
from .models import *
from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.auth.forms import UserCreationForm

class AmountSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = amount
        fields = '__all__'


class UserCreation(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=50)
    # last_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    password1 = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)

    # phone_numbers = serializers.IntegerField()
    # images = serializers.ImageField()
    # district = serializers.CharField(max_length=50)
    # pincode = serializers.IntegerField()

    class Meta():
        model = CustomUser
        fields =['username','email','address','password1','password2']

class loginseialize(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

#
# from django.db import transaction
# from rest_framework import serializers
# from dj_rest_auth.registration.serializers import RegisterSerializer
#
#
#
#
# class CustomRegisterSerializer(RegisterSerializer):
#     # gender = serializers.ChoiceField(choices=GENDER_SELECTION)
#     phone_number = serializers.CharField(max_length=30)
#
#     # Define transaction.atomic to rollback the save operation in case of error
#     @transaction.atomic
#     def save(self, request):
#         user = super().save(request)
#         # user.gender = self.data.get('gender')
#         print(self.data.get('phone_number'))
#         user.phone_number = "+919746814920"
#         user.save()
#         return user

#
# {
#     "username":"abb",
#     "email":"abb@gmail.com",
#     "password1":"abhin0202",
#     "password2":"abhin0202"
# }



# from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name','phone_number')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password1": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number']
        )

        user.set_password(validated_data['password1'])
        user.save()

        return user


class ProductAdd(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = product
        fields = ('id', 'product_name', 'product_category', 'images', 'details', 'price')

        def create(self, validated_data):
            id = validated_data['id']
            userdata = CustomUser.objects.get(id=id)
            productdata = product.objects.create(
                product_name=validated_data['product_name'],
                priduct_category=validated_data['priduct_category'],
                price=validated_data['price'],
                details=validated_data['details'],
                images=validated_data['images'],
                created_by=userdata
            )

            productdata.set_password(validated_data['password1'])
            productdata.save()

            return productdata

###########for login with token
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#
#
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)
#
#         # Add custom claims
#         token['username'] = user.username
#         return token