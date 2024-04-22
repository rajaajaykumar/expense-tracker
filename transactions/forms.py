from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount", "date", "category", "note"]
        widgets = {
            "category": forms.Select(attrs={"placeholder": "Select Category"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"placeholder": "Amount (₹)"}),
            "note": forms.TextInput(attrs={"placeholder": "Add note"}),
        }
