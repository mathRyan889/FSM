from django.contrib import admin
from .models import Category, Transaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user')
    search_fields = ('name',)
    list_filter = ('type',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'card','type', 'amount', 'date')
    search_fields = ('account__name', 'card__name', 'type')
    list_filter = ('date', 'type','is_recurring')
