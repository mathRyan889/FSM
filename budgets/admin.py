from django.contrib import admin
from .models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'month', 'year', 'alert_sent', 'created_at')
    list_filter = ('user', 'category', 'month', 'year')
    search_fields = ('user__user__username', 'category__name')
