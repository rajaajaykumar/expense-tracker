from django.shortcuts import render
from .models import Category, Transaction
from .forms import TransactionForm

# Create your views here.
def dashboard(request):
    """
    View to display the dashboard, that includes three recent transactions, account sumary and a form to add new transaction.
    """
    recent_transactions = Transaction.objects.order_by("-date")[:3]
    total_income = 0
    total_expense = 0
    total_balance = 0

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
    total_income = 0
    total_expense = 0
    total_balance = 0

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
