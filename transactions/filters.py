from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Transaction, Category

class TransactionFilter(AutoRQLFilterClass):
    MODEL = Transaction

class CategoryFilter(AutoRQLFilterClass):
    MODEL = Category