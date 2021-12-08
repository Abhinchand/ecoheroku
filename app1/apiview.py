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
from rest_framework import status
from rest_framework import serializers
from . models import *
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
    data = s("json", data1, fields=('product_name', 'product_category','images','details','price'))
    return HttpResponse(data, content_type='application/json')

    # return JsonResponse(data,safe=False)
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def userlogin(request):
    if request.method=='POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # print(user)
        # print(user.images.url)
    try:
        result = user.is_authenticated
        # status = user.is_active
        print(user.is_authenticated)
        data={
             'result' :{
                 'id':user.id,
                 'name':user.username,
                 'email':user.email,


                         }
                }
    except:
        
        data={
        'result':False
        }
    # data = json.dumps(data)

    return JsonResponse(data,safe=False)


@csrf_exempt
def UserRegister(request):
    result_data=None
    # form = apiuserform(request.POST)
    if request.method=='POST':
        form = apiuserform(request.POST)
        if form.is_valid():

            form = form.save(commit=False)
            form.type = 0
            form.is_active = True
            # form.is_active = False
            form.save()
            result_data=True


        # user = authenticate(request, username=username, password=password)

    if result_data:

        data={
            'result' :'True'
        }
    else:
        print(list(form.errors))
        error_data=form.errors
        # print(type(a))
        error_dict={}
        for i in list(form.errors):
            error_dict[i]=error_data[i][0]

        data={
            'resilt':False,
            'errors':error_dict
        }
    # data = json.dumps(data)

    return JsonResponse(data,safe=False)




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
        detail = [ {"user_id": detail.user_id,"amount": detail.amount}
                   for detail in amount.objects.all()]
        return Response(detail)

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)


class AmountItem(APIView):
    def get(self,request):
        details = [{"user_id":details.user_id,"amount":details.amount} for details in amount.objects.all()]
        return Response(details)

    def post(self,request):
        serializer = AmountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status.HTTP_400_BAD_REQUEST)