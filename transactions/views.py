from django.shortcuts import render
from .models import Category, Transaction

# Create your views here.
def dashboard(request):
    """
    View to display the dashboard
    """
    context = {}
    return render(request, "transactions/dashboard.html", context)


def transactions(request):
    """
    View to display all the historical transactions
    """
    context = {}
    return render(request, "transactions/transactions.html", context)
