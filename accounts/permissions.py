from rest_framework.permissions import BasePermission

class CreateActivityPermission(BasePermission):
    def has_permission(self, request, view):
        super_user = request.user.is_superuser
        staff = request.user.is_staff
        if staff or super_user:
            return True
        if request.method == 'POST':
            return True
        if request.method == 'GET':
            return True

class CoursePermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        super_user = request.user.is_superuser
        if super_user:
            return True
            
class FilterStudentActivity(BasePermission):
    def has_permission(self, request, view):
        super_user = request.user.is_superuser
        staff = request.user.is_staff
        if staff or super_user:
            return True
        if request.method == 'POST':
            return True
