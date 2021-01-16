from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import orderfilter
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Create your views here.
@authenticate_users
def register(request):
    form= registerform()
    if request.method == "POST":
        form= registerform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            return redirect ('login')

    context={'form':form}
    return render(request,'accounts/register.html',context)
@authenticate_users
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect ('home')
    context={}
    return render(request,'accounts/login.html',context)

def logoutpage(request):
    logout(request)
    return redirect ('login')





@login_required()
@adminoruser
def home(request):
    customers=Customer.objects.all()
    orders = Order.objects.all()
    total_orderd=orders.count()
    delivered=(Order.objects.filter(status='Delivered')).count()
    pending_order= orders.filter(status='pending').count()
    context={'customers':customers,'orders':orders,'total_orderd':total_orderd,'delivered':delivered,'pending_order':pending_order}
    return render(request,'accounts/dashboard.html',context)

@login_required()
@allowed_users(allowed_roles=['admin'])

def customer(request,pk):
    customer =  Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    myfilter = orderfilter(request.GET,queryset=orders)
    orders = myfilter.qs

    totalorders= orders.count()
    context={'customer':customer,'orders':orders,'total':totalorders, 'myfilter':myfilter}
    return render(request,'accounts/customer.html',context)

@login_required()
@allowed_users(allowed_roles=['customer'])
def userpage (request):
    context={}
    return render(request, 'accounts/user.html',context)

@login_required()
def myaccount (request):
    customer= request.user.customer
    form= customer_Form(instance=customer)
    if request.method =="POST":
        form= customer_Form(request.POST,request.FILES, instance=customer)

        if form.is_valid:
            form.save()
    context={'form':form}
    return render(request, 'accounts/myaccount.html',context)




@login_required()
@allowed_users(allowed_roles=['admin'])
def product(request):
    products = Product.objects.all()
    return render(request,'accounts/product.html',{'products':products})

@login_required()
@allowed_users(allowed_roles=['admin'])
def create_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
    customer= Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method =="POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,'accounts/orderform.html',context)
@login_required()
@allowed_users(allowed_roles=['admin'])
def create_customer(request):
    form= customer_Form()
    if request.method =="POST":
        form= customer_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'customerForm':customer_Form}
    return render(request,'accounts/customerform.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def update_order(request,pk):
    order =Order.objects.get(id=pk)
    form = order_Form(instance=order)
    if request.method =="POST":
        form= order_Form(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'upform':form}
    return render(request,'accounts/orderform.html',context)




@login_required()
@allowed_users(allowed_roles=['admin'])
def delete_order(request,pk):
    order= Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'item':order}
    return render (request,'accounts/delete.html',context)
