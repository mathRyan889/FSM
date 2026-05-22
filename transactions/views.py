from rest_framework import viewsets
from core.permissions import IsOwnerOfObject
from .filters import TransactionFilter, CategoryFilter
from rest_framework.permissions import DjangoModelPermissions
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    rql_filter_class = CategoryFilter
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfObject]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    rql_filter_class = TransactionFilter
    serializer_class = TransactionSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfObject]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(account__user__user=user)
        # vai checar se obj tem account e se esse account tem user (UserProfile) e se
        #  esse UserProfile tem user (Django User)