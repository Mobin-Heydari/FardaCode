from rest_framework import permissions



class IsStaffOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow staff or the user themselves to access the view.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff