from rest_framework import permissions
from rest_framework.views import View, Request


class isAdminListUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == "GET" and request.user.is_superuser:
            return True

        if request.method == "POST":
            return True
