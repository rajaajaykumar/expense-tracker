from django.shortcuts import render
from .models import Category, Transaction
from .forms import TransactionForm


def dashboard(request):
    """
    View to display the dashboard, that includes three recent transactions, account sumary and a form to add new transaction.
    """
    recent_transactions = Transaction.objects.order_by("-date")[:3]

    all_transactions = Transaction.objects.all()
    total_income = sum(transaction.amount for transaction in all_transactions if transaction.category.type == "Income") if all_transactions else 0
    total_expense = sum(transaction.amount for transaction in all_transactions if transaction.category.type == "Expense") if all_transactions else 0
    total_balance = total_income - total_expense

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionForm()

    context = {
        "form": form,
        "recent_transactions": recent_transactions,
        "total_income": total_income,
        "total_expense": total_expense,
        "total_balance": total_balance
    }
    return render(request, "transactions/dashboard.html", context)


def transactions(request):
    """
    View to display all the historical transactions and a form to add new transaction.
    """
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionForm()
    
    all_transactions = Transaction.objects.all().order_by("-date")
    total_income = sum(transaction.amount for transaction in all_transactions if transaction.category.type == "Income") if all_transactions else 0
    total_expense = sum(transaction.amount for transaction in all_transactions if transaction.category.type == "Expense") if all_transactions else 0
    total_balance = total_income - total_expense

    # Check if there are no transactions
    if not all_transactions:
        all_transactions = []
    
    context = {
        "form": form,
        "all_transactions": all_transactions,
        "total_income": total_income,
        "total_expense": total_expense,
        "total_balance": total_balance
    }
    return render(request, "transactions/transactions.html", context)
