from dj_rql.filter_cls import AutoRQLFilterClass
from .models import UserProfile

class UserProfileFilter(AutoRQLFilterClass):
    MODEL = UserProfile