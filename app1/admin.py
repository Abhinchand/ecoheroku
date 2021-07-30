from django.contrib import admin

from .models import *

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser

class coustomadmin(admin.ModelAdmin):
    list_display = ["product_name","update","timestamp"]
    list_display_links = ["update"]
    list_editable = ["product_name"]
    list_filter = ["update","timestamp"]
    search_fields = ["product_name"]

    class Meta:
        model = product

admin.site.register(product,coustomadmin)

admin.site.register(CustomUser)
admin.site.register(cart)
admin.site.register(amount)
admin.site.register(product_payed)
admin.site.register(paytrack)
admin.site.register(delivery_address)
admin.site.register(feedback)
