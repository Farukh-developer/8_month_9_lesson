from rest_framework.permissions import BasePermission, SAFE_METHODS




class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if request.user.is_staff:
            return True
        
    
