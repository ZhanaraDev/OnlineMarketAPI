from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    """
    fix_an_appointment
    """

    def has_permission(self, request, view):
        print("bububl",request.user.is_authenticated)
        if request.user.is_authenticated:
            if view.action == 'delete' or view.action == 'create':
                return request.user.is_superuser
            else:
                return True
        return False