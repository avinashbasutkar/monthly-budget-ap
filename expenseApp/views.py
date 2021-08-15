from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transactions
from django.db.models import Sum

# Create your views here.

def home(request):
    transactions = Transactions.objects.all()
    itemPriceTotal = Transactions.objects.all().aggregate(Sum('itemPrice'))
    return render(request, "expenseApp/home.html", {'transactions':transactions, 'itemPriceTotal':itemPriceTotal})

def addTransaction(request):
    if request.method == 'POST':
        new_transaction = Transactions(
            itemName = request.POST['itemname'],
            itemPrice = request.POST['amount'],
            transactionDate = request.POST['datetime'],
            category = request.POST['category'],
        )
        new_transaction.save()
        return redirect('/')
        
    return render(request, "expenseApp/addTransaction.html")

def transDetail(request, transaction_id):
    transactions = Transactions.objects.get(id=transaction_id)
    return render(request, "expenseApp/transDetail.html", {'transactions':transactions})

def login(request):
    return render(request, "expenseApp/login.html")