from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissions():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]