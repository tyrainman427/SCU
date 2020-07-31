from django.urls import path
from .views import EmployeeList, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

app_name = 'employee'

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('<int:id>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('new/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<pk>/update-employee/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<pk>/delete-employee/', EmployeeDeleteView.as_view(), name='employee-delete'),

]
