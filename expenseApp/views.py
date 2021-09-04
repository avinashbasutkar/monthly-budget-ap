from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from .models import Transactions
from django.db.models import Sum
from django.contrib import messages

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
    return render(request, "expenseApp/transactions_form.html", {'transactions':transactions})

def updateExpense(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)
    transaction.itemName = request.POST.get('itemname')
    transaction.save()
    messages.success(request, 'Expense updated!')
    return redirect('/')

class updateExpenseView(UpdateView):
    model = Transactions

    fields = [
        "itemName",
        "itemPrice",
        "category"
    ]

    success_url = "/"

def deleteExpense(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)
    transaction.delete()
    messages.success(request, 'Expense removed!')
    return redirect('/')

def login(request):
    return render(request, "expenseApp/login.html")