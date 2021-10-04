from .forms import *
from django.contrib.auth.decorators import login_required
# from django.utils import simplejson
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core import serializers


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
    qs_json = serializers.serialize('json', data)
    data = serialize("json", data1, fields=('product_name', 'product_category','images','details','price'))
    return HttpResponse(data, content_type='application/json')

    # return JsonResponse(data,safe=False)
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def userlogin(request):
    if request.method=='POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        # print(email)

        user = authenticate(request, username=username, password=password)
    try:
        result = user.is_authenticated
        print(user.is_authenticated)
        data={
             'result' :result
                }   
    except:
        
        data={
        'resilt':False
        }
    # data = json.dumps(data)

    return JsonResponse(data,safe=False)



