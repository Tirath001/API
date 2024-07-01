from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, 
    MyTokenObtainPairView, 
    UserDetailView,
    EmployeeProfileViewSet,
    AttendanceViewSet,
    SalaryViewSet,
    ProjectViewSet,
    LeaveViewSet,
    LogoutView
)

router = DefaultRouter()
router.register(r'employeeprofiles', EmployeeProfileViewSet, basename='employeeprofile')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'salaries', SalaryViewSet, basename='salary')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'leaves', LeaveViewSet, basename='leave')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
