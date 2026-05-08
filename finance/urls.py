from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewset, CardViewset

router = DefaultRouter()
router.register('account', AccountViewset)
router.register('card', CardViewset)

urlpatterns = [
    path('', include(router.urls)),
]
