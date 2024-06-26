from django.db import models
from django.utils import timezone


class Category(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("Expense", "Expense"),
        ("Income", "Income")
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)

    def __str__(self) -> str:
        return f"{self.type} - {self.name}"


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=False, editable=True, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Set the date field to the current date and time only if the object is being created
            self.date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        formatted_date = self.date.strftime("%Y-%m-%d %H:%M:%S")
        return f"{formatted_date} - ₹{self.amount} - {self.category}"
