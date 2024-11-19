from rest_framework.permissions import BasePermission


http_methods = ['GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE']


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in http_methods:
            return True
        return bool(request.user.is_authenticated and request.user.is_superuser)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in http_methods:
            return True
        return bool(request.user.is_authenticated and request.user.role == "admin")


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in http_methods:
            return True
        return obj.user == request.user


class IsDriver(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in http_methods:
            return True
        return obj.driver == request.user

