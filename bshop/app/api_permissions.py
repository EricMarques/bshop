from rest_framework.permissions import BasePermission


class OnlyAdminCanCreate(BasePermission):
    @staticmethod
    def has_permission(request):
        if request.method == 'POST':
            return request.user.is_staff
        return True


class OnlyAdminCanDelete(BasePermission):
    @staticmethod
    def has_permission(request):
        if request.method == 'DELETE':
            return request.user.is_staff
        return True


class OnlyAdminCanPut(BasePermission):
    @staticmethod
    def has_permission(request):
        if request.method == 'PUT':
            return request.user.is_staff
        return True


class OnlyAdminCanPatch(BasePermission):
    @staticmethod
    def has_permission(request):
        if request.method == 'PATCH':
            return request.user.is_staff
        return True


class OnlyAdminCanOptions(BasePermission):
    @staticmethod
    def has_permission(request):
        if request.method == 'OPTIONS':
            return request.user.is_staff
        return True


class OnlyGet(BasePermission):
    @staticmethod
    def has_permission(request):
        if (request.method == 'POST' or
                request.method == 'PUT' or
                request.method == 'DELETE' or
                request.method == 'PATCH' or
                request.method == 'OPTIONS'):
            return request.user.is_staff
        return True


class OnlyAdminCanMakeAnything(BasePermission):
    @staticmethod
    def has_permission(request, ):
        if (request.method == 'POST' or
                request.method == 'PUT' or
                request.method == 'DELETE'):
            return request.user.is_staff
