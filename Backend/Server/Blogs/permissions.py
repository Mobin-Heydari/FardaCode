from rest_framework import permissions




class IsSafeMethodOrStaff(permissions.BasePermission):
    """
        Custom permission to only allow staff or the user who just want to access the data.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff