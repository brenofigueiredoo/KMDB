from rest_framework import permissions
from rest_framework.views import View, Request
import ipdb


class isCriticOrIsAdm(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == "GET":
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.user.is_critic:
            return True

        return False
