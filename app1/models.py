from django.db import models
from PIL import Image
# Create your models here
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=128,null=True)
    last_name = models.CharField(max_length=128,null=True)
    email = models.EmailField(max_length=128,null=True)
    #images = models.ImageField(upload_to='abhin/')
    images = ResizedImageField(upload_to='uploads/%Y/%m/%d',null=True)
    address = models.TextField(max_length=200,null=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    pincode = models.IntegerField(null=True)
    district = models.CharField(max_length=50,null=True)
    type= models.IntegerField(null=True)
    # is_apiuser = models.BooleanField()




class delivery_address(models.Model):
    users=models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    user_id=models.IntegerField(null=True)
    d_name = models.CharField(max_length=128)
    d_phone_number = PhoneNumberField(null=False, blank=False)
    d_district = models.CharField(max_length=50)
    d_pincode = models.IntegerField()
    d_address = models.TextField(max_length=200)
    d_pickup_time = models.TimeField(null=True)
    d_primary = models.BooleanField(default=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "-update"]





##Product models

class product(models.Model):

    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    images = models.ImageField(upload_to='products/')
    details = models.CharField(max_length=100)

    price = models.IntegerField()

    #created_by = models.IntegerField()
    created_by = models.ForeignKey(CustomUser,on_delete = models.CASCADE,null=True)


    update =models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.images.path)  # Open image using self

        new_img = (300, 300)
        img.thumbnail(new_img)
        img.save(self.images.path)  # saving image at the same path


    def __unicode__(self):
        return self.product_name
    def __str__(self):
        return self.product_name

    class Meta:
        ordering=["-timestamp","-update"]



class cart(models.Model):
    product_id=models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    images = models.ImageField(upload_to='cart/')
    price = models.IntegerField()
    price_base = models.IntegerField()
    quantity = models.IntegerField(null=True)
    created = models.IntegerField()
    update = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.product_name

    def __str__(self):
        return self.product_name


class amount(models.Model):
    user_id=models.IntegerField()
    amount=models.IntegerField()


class product_payed(models.Model):
    pay_id = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    d_address = models.ForeignKey(delivery_address,on_delete = models.CASCADE,null=True)
    paydate= models.DateField(null=True)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    images = models.ImageField(upload_to='tarck/')
    price = models.IntegerField()
    price_base = models.IntegerField()
    quantity = models.IntegerField(null=True)
    created = models.IntegerField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    delivery_status = models.BooleanField(null=True,default=False)

    def __unicode__(self):
        return self.product_name

    def __str__(self):
        return self.product_name
class paytrack(models.Model):
    user_id = models.IntegerField(null=True)
    paydate= models.DateField(null=True)
    item = models.IntegerField()
    delivery_status=models.BooleanField(null=True,default=False)

    prodcut_data = models.ManyToManyField(product_payed)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "-update"]

class feedback(models.Model):
    user_details = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    feedback_text = models.TextField()
    update = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)




    class Meta:
        ordering = ["-timestamp","-update"]




