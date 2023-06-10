from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    IMPORTANT!!! I have changed this to author to match the reviews model
    Remember this for future model uses if necessary
    ---------------------------------------------------------------------
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    Taken from
    https://www.django-rest-framework.org/api-guide/permissions/#examples
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # IMPORTANT!!!
        # Changed from example to match author attribute on reviews model
        return obj.author == request.user
