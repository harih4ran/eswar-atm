from django.shortcuts import render,redirect
from accounts.models import *
from accounts.forms import *
from django.contrib.auth.decorators import login_required

def CustomerView(request): 
    customers = Customer.objects.all()
    form = CustomerForm() 
    context = {
        'form':form,
        'customers':customers,
    }
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers') 

    return render(request,"customer/index.html",context)  

def AccountsView(request): 
    accounts = Account.objects.all()
    form = AccountForm() 
    context = {
        'form':form,
        'accounts':accounts,
    }
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts') 

    return render(request,"accounts/index.html",context) 

def WithdrawView(request): 
    customers = Customer.objects.all()
    form = CustomerForm() 
    context = {
        'form':form,
        'customers':customers,
    }
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 

    return render(request,"withdraw/index.html",context) 


