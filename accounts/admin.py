from django.contrib import admin
from .models import Account, Transaction
# Register the Account model
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user',)
    readonly_fields = ('balance',)

# Register the Transaction model
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'date')
    search_fields = ('account__user__username', 'transaction_type')
    list_filter = ('transaction_type', 'date')
    readonly_fields = ('date',)

