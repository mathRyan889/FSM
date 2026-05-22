from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Budget

class BudgetFilter(AutoRQLFilterClass):
    MODEL = Budget