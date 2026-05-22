from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from core.permissions import IsOwnerOfObject
from .filters import BudgetFilter
from .models import Budget
from .serializers import BudgetSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    rql_filter_class = BudgetFilter
    permission_classes = [DjangoModelPermissions, IsOwnerOfObject]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Budget.objects.all()
        return Budget.objects.filter(user__user=user)
    
    # vai checar se obj tem user (UserProfile) e se esse UserProfile tem user (Django User)
