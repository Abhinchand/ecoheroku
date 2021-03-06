from .forms import *
from django.contrib.auth.decorators import login_required
# from django.utils import simplejson
from django.http import HttpResponse
from django.http import JsonResponse

##################  serializer ##################
from django.core.serializers import serialize as s
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import serializers
from .models import *
from .serializer import *

##################  end serializer ###############
from django.http import HttpResponse
import json

from django.contrib.auth import authenticate, login


def some_view(request):
    # data=CustomUser.objects.all()
    data = list(CustomUser.objects.filter(is_superuser=True))
    data1 = product.objects.all()

    to_json = {
        "key1": "value1",
        "key2": "value2"
    }
    # qs_json = serializers.serialize('json', data)
    data = s("json", data1, fields=('product_name', 'product_category', 'images', 'details', 'price'))
    return HttpResponse(data, content_type='application/json')

    # return JsonResponse(data,safe=False)


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # print(user)
        # print(user.images.url)
    try:
        result = user.is_authenticated
        # status = user.is_active
        print(user.is_authenticated)
        data = {
            'result': {
                'id': user.id,
                'name': user.username,
                'email': user.email,

            }
        }
    except:

        data = {
            'result': False
        }
    # data = json.dumps(data)

    return JsonResponse(data, safe=False)


@csrf_exempt
def UserRegister(request):
    result_data = None
    # form = apiuserform(request.POST)
    if request.method == 'POST':
        form = apiuserform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.type = 0
            form.is_active = True
            # form.is_active = False
            form.save()
            result_data = True

        # user = authenticate(request, username=username, password=password)

    if result_data:

        data = {
            'result': 'True'
        }
    else:
        print(list(form.errors))
        error_data = form.errors
        # print(type(a))
        error_dict = {}
        for i in list(form.errors):
            error_dict[i] = error_data[i][0]

        data = {
            'resilt': False,
            'errors': error_dict
        }
    # data = json.dumps(data)

    return JsonResponse(data, safe=False)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.type = 0
            form.is_active = False
            # form.is_active = False
            form.save()


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = amount
        fields = ['user_id', 'amount']


class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        detail = [{"user_id": detail.user_id, "amount": detail.amount}
                  for detail in amount.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class AmountItem(APIView):
    def get(self, request):
        details = [{"user_id": details.user_id, "amount": details.amount} for details in amount.objects.all()]
        return Response(details)

    def post(self, request):
        serializer = AmountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status.HTTP_400_BAD_REQUEST)


# from dj_rest_auth.registration.serializers import RegisterSerializer
class UserCreationApi(APIView):

    def post(self, request):
        userdata = RegisterSerializer(data=request.data)
        if userdata.is_valid():
            userdata.save()
            return Response({"status": "success", "data": userdata.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": userdata.errors}, status.HTTP_400_BAD_REQUEST)


class UserLoginApi(APIView):

    def post(self, request):
        # userdata =loginseialize(data=request.data)
        d = request.POST.get('username')
        print('gg', d)
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            return Response({"status": "success", "data": [
                {"Username": user.username,
                 "email": user.email,
                 "id": user.id}]}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": 'useename and password is invalid'},
                            status.HTTP_400_BAD_REQUEST)


# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView

###for login with access tocken
# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer
#
#






# from rest_framework_simplejwt.tokens import AccessToken
# from django.contrib.auth.models import User
#
# access_token_str = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MTIzMjg2LCJpYXQiOjE2MzkxMjI5ODYsImp0aSI6IjdhY2EzMjMwNWVmNTRkZWJhYmFiMTJlODc5YzY3YTI3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhYmhpbiJ9.WYLphfKQTaOMHLmdRkTPWBnji6Niy6BOR8-irFnJqcw'
# def get_user_from_access_token_in_django_rest_framework_simplejwt(access_token_str):
#     access_token_obj = AccessToken(access_token_str)
#     user_id=access_token_obj['user_id']
#     user=User.objects.get(id=user_id)
#     print('user_id: ', user_id )
#     print('user: ', user)
#     print('user.id: ', user.id )
#     content =  {'user_id': user_id, 'user':user, 'user.id':user.id}
#     return Response(content)

class ViewProtect(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        token_user_email = request.user.email
        token_user_username = request.user.username
        pass


class Product(APIView):
    def get(self, request):
        details = [{"id": details.id,
                    "product_name": details.product_name,
                    "product_category": details.product_category,
                    "price": details.price,
                    "images": details.images.url,
                    "details": details.details,
                    "created": details.created_by.username} for details in product.objects.all()]
        return Response(details)

    def post(self, request):
        serializer = ProductAdd(data=request.data)
        # id=request.POST.get("id")
        # print(id)
        # user =CustomUser.objects.get(id=id)
        if serializer.is_valid():
            # serializer=serializer.save(commit=False)
            # serializer.created_by = user
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status.HTTP_400_BAD_REQUEST)
