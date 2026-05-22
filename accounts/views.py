from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

from accounts.filters import UserProfileFilter
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    rql_filter_class = UserProfileFilter
