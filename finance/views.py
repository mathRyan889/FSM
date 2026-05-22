from rest_framework import viewsets
from core.permissions import IsOwnerOfObject
from .filters import AccountFilter, CardFilter
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Account, Card
from .serializers import AccountSerializer, CardSerializer


class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    rql_filter_class = AccountFilter
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Account.objects.all()
        return Account.objects.filter(user__user=user)
        # vai checar se obj tem user (UserProfile) e se esse UserProfile tem user (Django User)


class CardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    rql_filter_class = CardFilter
    permission_classes = [DjangoModelPermissions, IsOwnerOfObject]

    def get_queryset(self):

        user = self.request.user
        if user.is_staff:
            return Card.objects.all()
        return Card.objects.filter(account__user__user=user)
        # vai checar se obj tem account e se esse account tem user (UserProfile) e se
        #  esse UserProfile tem user (Django User)
