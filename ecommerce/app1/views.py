from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date,timedelta
import random as rm
# Create your views here.
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
a=5

def test(request):
    return render (request,'userdata.html')

def base(request):
    return render (request,'base.html')


def signup(request):
    return render (request,'registration/signup.html')

def index(request):
    return render(request,'index.html')
def track_list(request):
    return render(request,'tracking_list.html')
@login_required()
def userpanel(request):
    instance = cart.objects.filter(created=request.user.id)
    instance = len(instance)
    print('innnn',instance)
    context ={
        "length":instance
    }
    return render(request,'userpanel.html',context)
@login_required()
def cart_items(request):
    return render(request,'cart.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.type=0
            form.is_active = False
            #form.is_active = False
            form.save()


            return redirect('login')

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required()
def userview(request):

    type = request.user.type
    if type == 1:
        return redirect('view_product_admin')

    else:
        #return render(request, 'userpanel.html', {})
        return redirect('view_product')

######################Retrive#########################



def create_product(request):
    form = Form_product(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        #messages.success(request, "successfilly created")
        return redirect("create_product")
        #return render(request,"list.html")
    context ={
        'form': form,
    }
    return render(request, "create_product.html", context)

def add_to_cart(request,id=None):
    form = Form_cart(request.POST)
    instance1= request.POST.get('quantity')
    print('hi',instance1)
    if form.is_valid:
        instance = get_object_or_404(product,id=id)
        c_id=request.user.id
        cart.objects.create(product_id=instance.id,
                               product_name=instance.product_name,
                               product_category=instance.product_category,
                               images=instance.images,
                               quantity=1,
                               price=instance.price,
                               price_base=instance.price,
                               created=c_id,
                              )
    total_price(request.user.id)
    return redirect('view_product')

def total_price(id=None):
    uid = id
    data = cart.objects.filter(created=uid)
    #instance = get_object_or_404(amount,user_id=id)
    instance = amount.objects.filter(user_id=id)
    instance.delete()

    global amount_product
    amount_product =0
    for data in data:
        amount_product +=data.price
        print('check',data.price)

    amount.objects.create(user_id=uid,
                        amount=amount_product,)
    return




def add_quantity(request,id=None):
    instance= get_object_or_404(cart,id=id)
    p_id=instance.product_id
    print('pid',p_id)
    instance1=get_object_or_404(product,id=p_id)
    instance1=instance1.price
    print(instance1)
    if instance.quantity >=1:
        instance.quantity +=1
        print('price',instance.quantity)
        instance.price =instance1*instance.quantity
        print('price',instance.price)
        instance.save()
        total_price(request.user.id)
    return redirect('view_cart')

def remove_quantity(request,id=None):
    instance = get_object_or_404(cart,id=id)
    p_id = instance.product_id
    print('pid', p_id)
    instance1 = get_object_or_404(product, id=p_id)
    instance1 = instance1.price
    if instance.quantity >=2:
        instance.quantity -=1
        instance.price -=instance1
        instance.save()
        total_price(request.user.id)
    return redirect('view_cart')


######################Retrive#########################
@login_required()
def view_products(request):
    instance1 = cart.objects.filter(created=request.user.id)
    instance1 = len(instance1)
    instance= product.objects.filter()
    context ={
        "obj_list":instance,
        'user_data':request.user.username,
        "length": instance1
    }
    return render(request,"item_view.html",context)
@login_required()
def view_products_admin(request):
    instance1 = cart.objects.filter(created=request.user.id)
    instance1 = len(instance1)


    instance= product.objects.all()


    context ={
        "obj_list":instance,
        "length": instance1
    }
    return render(request,"item_view_admin.html",context)
@login_required()
def view_products_backery(request):
    instance= product.objects.all()
    instance1 = cart.objects.filter(created=request.user.id)
    instance1 = len(instance1)


    context ={
        "obj_list":instance,
        "type":'Backery',
        "length":instance1
    }
    return render(request,"item_view_backery.html",context)
@login_required()
def view_products_fruits(request):
    instance = product.objects.all()
    instance1 = cart.objects.filter(created=request.user.id)
    instance1 = len(instance1)


    context ={
        "obj_list":instance,
        "type":'Fruits',
        "length": instance1
    }
    return render(request,"item_view_fruits.html",context)
@login_required()
def view_products_vegitable(request):
    instance= product.objects.all()
    instance = product.objects.all()
    instance1 = cart.objects.filter(created=request.user.id)
    instance1 = len(instance1)


    context ={
        "obj_list":instance,
        "type":'Vegitable',
        "length": instance1
    }
    return render(request,"item_view_vegitable.html",context)
@login_required()
def view_products_own(request):
    instance = product.objects.all()
    instance1 = cart.objects.filter(created=request.user.id)
    instance1 = len(instance1)
    context ={
        "obj_list":instance,
        "user":request.user,
        "length": instance1
    }
    return render(request,"item_view_own.html",context)

########userdata#######
@login_required()
def userdatas(request):
    instance = CustomUser.objects.all()
    context={
        "obj_list":instance,

    }
    return  render(request,'userdata.html',context)
@login_required()
def view_cart(request):
    instance = cart.objects.all()
    print(request.user.id)
    #instance1 = amount.objects.all(user_id=request.user.id)
    # instance1 = get_object_or_404(amount,user_id=request.user.id)
    try:
        instance1 = get_object_or_404(amount,user_id=request.user.id)

        address = delivery_address.objects.get(users = request.user,d_primary=True)
    except:
        address=''
        instance1=''



    context = {
        "obj_list":instance,
        "user": request.user.id,
        "amount_data":instance1,
        "address":address,

    }
    return render(request,'cart.html',context)
@login_required()
def track_order(request,id=None):
    
    instance = product_payed.objects.filter(created = request.user.id)
    address = delivery_address.objects.get(users = request.user,d_primary=True)
    instance1 = paytrack.objects.get(id = id)
    many_data = instance1.prodcut_data.all()
    for date_p in many_data:
        date_p=date_p.paydate

    for d_ad in many_data:
        users=d_ad.d_address.users
        d_name=d_ad.d_address.d_name
        d_phone_number=d_ad.d_address.d_phone_number
        d_district=d_ad.d_address.d_district
        d_pincode=d_ad.d_address.d_pincode
        d_address=d_ad.d_address.d_address
        d_pickup_time=d_ad.d_address.d_pickup_time
        date_p=d_ad.paydate
        od_id =d_ad.order_id
        d_id=d_ad.id

    mydata={'users':users,'d_name':d_name,'d_phone_number':d_phone_number,'d_district':d_district,'d_pincode':d_pincode,'d_address':d_address,'d_pickup_time':d_pickup_time,'date':date_p,'order_id':od_id}

    length = len(instance)

    context = {
        "date":date_p,
        "length":length,
        "mydata":mydata,
        "address":address,
        "instance":instance1,
        "many_data":many_data,
        'd_id':instance1

    }
    return render(request,'tracking.html',context)




def track_list(request):
    instance = paytrack.objects.filter(user_id=request.user.id,delivery_status=False)
    # for inn in instance:
    #     print(inn.user_id)
    #     inn=inn.prodcut_data.all()
    
    #     print(inn)
    # data1=zip(instance,inn)
    context={
        "instance":instance,
        # "data":inn,
        # "data1":data1,
    }

    return render(request,'tracking_list.html',context)

######################Retrive#########################
@login_required()
def Delivery_address(request):

    form = Form_address(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.users=request.user
        instance.user_id=request.user.id
        instance.save()
        #messages.success(request, "successfilly created")
        return redirect("manage_address")
        #return render(request,"list.html")
    context ={
        'form': form,
    }
    return render(request, "delivery_address.html", context)

@login_required()
def payform(request):
    data=delivery_address.objects.filter(users=request.user,d_primary=True)
    if data:
        instance1 = get_object_or_404(amount,user_id=request.user.id)
    else:
        data=delivery_address.objects.filter(users=request.user)
        if not data:
            return redirect('delivery_address')
        data=delivery_address.objects.filter(users=request.user,d_primary=True)
        if not data:
            return redirect('manage_address')



    print(data)
    # try:
    #     delivery_address.objects.filter(users=request.user,d_primary=True)
    #
    # except:
    #     return redirect('manage_address')


    context ={
    "obj_list":instance1

    }

    return render(request,'paymentform.html',context)
@login_required()
def manage_address(request):
    instance1 = delivery_address.objects.filter(user_id=request.user.id)

    context ={
    "obj_list":instance1

    }

    return render(request,'manage_address.html',context)
@login_required()
def payed(request,id=None):
    instance = cart.objects.filter(created=request.user.id)
    address_data = delivery_address.objects.get(users=request.user,d_primary=True)
    print('address',address_data.d_name)

    instance1 = get_object_or_404(amount,user_id=request.user.id)
    instance_amount = get_object_or_404(amount,user_id=request.user.id)
    dt = date.today() + timedelta(days=2)
    pay_product_data=paytrack.objects.create(user_id=request.user.id,
                            paydate=dt,
                            item=len(instance),
                            )
    global order_id_num
    order_id_num=rm.randint(12479325879,789321566999)
    for instance in instance:
        data=product_payed.objects.create(pay_id=request.user.id+1,
                                     order_id=order_id_num,
                                     d_address =address_data,
                                     paydate=dt,
                                     product_id=instance.product_id,
                                     product_name=instance.product_name,
                                     product_category=instance.product_category,
                                     images=instance.images,
                                     price=instance.price,
                                     price_base=instance.price_base,
                                     quantity=instance.quantity,
                                     created=instance.created,

        )
        pay_product_data.prodcut_data.add(data)
        pay_product_data.save()

        instance.delete()
    instance_amount.amount=0
    instance_amount.save()
    dt = date.today()
    instance = product_payed.objects.filter(created=request.user.id)

    context ={
        "amt":instance1,
        "obj_list":instance,
        "date":dt,
        "order_id":order_id_num,

    }
    return render(request,'invoice.html',context)



######################Updates#########################

@login_required()
def update_products(request, id=None):
    instance = get_object_or_404(product, id=id)
    form = Form_product(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance =form.save(commit=False)
        instance.save()
        messages.success(request, "successfilly updated")

        return redirect('view_product_own')
    context={

        'instance':instance,

        'form' :form,
    }
    return render(request,"update_product.html",context)



@login_required()
def update_delivery_address(request, id=None):
    instance = get_object_or_404(product, id=id)
    form = Form_address(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance =form.save(commit=False)
        instance.save()
        messages.success(request, "successfilly updated")

        return redirect('manage_address')
    context={

        'instance':instance,

        'form' :form,
    }
    return render(request,"delivery_address.html",context)





######################Delete#########################

@login_required()
def delete_product(request,id=None):
    instance= get_object_or_404(product,id=id)
    instance.delete()
    messages.success(request, "successfilly Deleted")
    return redirect('view_product_own')
@login_required()
def delete_cart(request,id=None):
    instance= get_object_or_404(cart,id=id)
    instance.delete()
    total_price(request.user.id)
    messages.success(request, "successfilly Removed From Cart")
    return redirect('view_cart')

@login_required()
def delete_delivery_address(request,id=None):
    instance= get_object_or_404(delivery_address,id=id)
    instance.delete()
    total_price(request.user.id)
    messages.success(request, "successfilly Deleted")
    return redirect('manage_address')






####extra
@login_required()
def set_primary_address(request,id=None):
    data = delivery_address.objects.filter(users=request.user)
    for data in data:
        data.d_primary=False
        data.save()

    instance= get_object_or_404(delivery_address,id=id)
    instance.d_primary=True
    instance.save()
    return  redirect('manage_address')

#######oreder details #######

@login_required()
def orderdetails(request):
    data=product_payed.objects.filter(product_id=request.user.id)
    data=product_payed.objects.all()

    data_list = []
    for data1 in data:
        product_data = product.objects.get(id=data1.product_id)
        if product_data.created_by == request.user:
            print('user',product_data.created_by)
            data_list.append(data1)
    print('data',request.user.id)
    print(data_list)

    return render(request,'orderdetails.html',{'data':data_list})

@login_required()
def orderdetailsview(request, id = None):
    data=product_payed.objects.get(id=id)


    print('data',data.d_address)

    return render(request,'orderdetailsview.html',{'data':data})
@login_required
def markasdelivered(request,id=None):
    data=product_payed.objects.get(id=id)
    data.delivery_status=True
    data.save()
    return redirect('orderdetailsview',id)
@login_required
def markasdelivereduser(request,id=None):
    data = paytrack.objects.get(id=id)
    data.delivery_status = True
    data.save()
    return redirect('view_tracking_list')


##### accounts activate and deactivate  #######
@login_required()
def activate(request,id=None):
    insatnce = get_object_or_404(CustomUser,id=id)
    insatnce.is_active = True
    insatnce.save()
    return redirect('view_userdata')


@login_required()
def deactivate(request,id=None):
    insatnce = get_object_or_404(CustomUser,id=id)
    insatnce.is_active = False
    insatnce.save()
    return redirect('view_userdata')

###### end #######

######### search field ########
def searchfield(request):
    name = request.GET['qqq']

    cat=(request.GET['cat'])
    print(name)
    if cat=='all':
        all_data = ['Fruits', 'Vegitable', 'Backery']
        data = product.objects.filter(product_name=name,product_category__in=all_data)  # filedsname__in  use for filter multiple data
    else:
        data = product.objects.filter(product_name=name, product_category=cat)

    print('cat',cat)

    print(data)
    context = {
        "obj_list": data,

    }
    return render(request, "item_view_search.html", context)


class SearchView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = product.objects.filter(
            Q(title__icontains=kw) | Q(description__icontains=kw) | Q(return_policy__icontains=kw))
        print(results)
        context["results"] = results
        return context


def FeedbackView(request,id=None):
    id=id
    if request.method == 'POST':
        form = Form_feedback(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user_details=request.user
            form.product = product.objects.get(id=id)
            form.save()


            return redirect('view_product')

    else:
        form = Form_feedback()

    return render(request, 'feedback.html', {'form': form})

def ViewFeedBack(request,id=None):
    product_data = product.objects.get(id=id)
    data = feedback.objects.filter(product=product_data)
    print(data)
    return render(request,'viewfeedback.html',{'data':data,'product_data':product_data})

def ViewFeedBackAdmin(request,id=None):
    product_data = product.objects.get(id=id)
    data = feedback.objects.filter(product=product_data)
    print(data)
    return render(request,'viewfeedbackAdmin.html',{'data':data,'product_data':product_data})

