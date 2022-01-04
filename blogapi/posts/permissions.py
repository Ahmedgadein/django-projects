from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if(request in permissions.SAFE_METHODS):
            return True

        return obj.author == request.user    