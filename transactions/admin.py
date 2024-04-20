from django.contrib import admin
from .models import Category, Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["date", "amount", "get_transaction_type", "note"]
    list_filter = ["date"]
    search_fields = ["note"]
    
    def get_transaction_type(self, transaction):
        return transaction.category.type if transaction.category else None

    get_transaction_type.short_description = "Type"

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category)
