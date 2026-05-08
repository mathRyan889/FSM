from django.contrib import admin
from .models import Account, Card


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'balance', 'bank_name', 'is_active', 'created_at')
    list_filter = ('type', 'is_active')
    search_fields = ('name', 'bank_name')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('account', 'name', 'credit_limit', 'used_limit', 'due_day', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'account__name')
