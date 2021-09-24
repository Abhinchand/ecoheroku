from .forms import *
from django.contrib.auth.decorators import login_required
# from django.utils import simplejson
from django.http import HttpResponse
from django.http import JsonResponse
def some_view(request):
    to_json = {
        "key1": "value1",
        "key2": "value2"
    }
    return JsonResponse(to_json)


def userview():
    CustomUser.objects.all()

