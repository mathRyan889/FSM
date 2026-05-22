from rest_framework import permissions


class IsOwnerOfObject(permissions.BasePermission):
    """
    Permissão que verifica se o usuário autenticado
    é o dono do objeto, seguindo a cadeia:

    Transaction → account → user (UserProfile) → user (Django User)
    Card        → account → user (UserProfile) → user (Django User)
    Account     → user (UserProfile) → user (Django User)
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Transaction ou qualquer obj com FK para Account
        if hasattr(obj, 'account'):
            return obj.account.user.user == user
            #               ↑            ↑
            #         UserProfile    Django User

        # Account direto
        if hasattr(obj, 'user') and hasattr(obj.user, 'user'):
            return obj.user.user == user
        # vai checar se obj tem user (UserProfile) e se esse UserProfile tem user (Django User)

        return False
