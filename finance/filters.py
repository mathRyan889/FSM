from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Account, Card

class AccountFilter(AutoRQLFilterClass):
    MODEL = Account

class CardFilter(AutoRQLFilterClass):
    MODEL = Card