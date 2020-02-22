from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import Customers,Products,Orders
from accounts.forms import OrderForm, ProductForm
def home(request):
    customer = Customers.objects.all
    product = Products.objects.all()
    order = Orders.objects.all()
    total_orders = len(order)
    pending = order.filter(status ='pending').count()
    delivered = order.filter(status = 'delivered').count()
    outfordelivery = order.filter(status = 'outfordelivery').count()
    context = {'customer':customer,'product':product,'order':order,
               'total_orders':total_orders,'pending':pending,
               'delivered':delivered,'outfordelivery':outfordelivery}
    return render(request,'crmaccounts/dashboard.html',context)

def products(request):
    product = Products.objects.all()


    context = {'product':product}
    return render(request, 'crmaccounts/products.html',context)
def customer(request,pk):
    customers = Customers.objects.get(id=pk)
    order = customers.orders_set.all()
    context = {'customers':customers,'order':order}
    return render(request,'crmaccounts/customer.html',context)

def orders(request,pk):
    pass
    return render(request, 'crmaccounts/orders.html')
def update_order(request,pk):
    order = Orders.objects.get(id=pk)
    form = OrderForm(instance = order)
    if request.method=="POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'crmaccounts/update_order.html',context)
def delete_order(request, pk):
    order = Orders.objects.get(id=pk)
    order.delete()
    return redirect('/')
def add_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        form = ProductForm()
        context = {'form':form}
        return render(request,'crmaccounts/add_product.html',context)

def update_product(request,pk):
    product = Products.objects.get(id=pk)
    if request.method=="POST":
        form = ProductForm(request.POST,instance=product,)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        form = ProductForm(instance=product)
        context = {'form':form}
        return render(request,'crmaccounts/update_product.html',context)

def delete_product(request,pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return redirect('/product')

def add_order(request):
    if request.method =="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm()
        context = {'form':form}
        return render(request,'crmaccounts/add_order.html',context)