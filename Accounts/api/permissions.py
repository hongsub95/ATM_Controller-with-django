from rest_framework.permissions import BasePermission
from administrators import models

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if 'admin-token' not in request.session:
            return False