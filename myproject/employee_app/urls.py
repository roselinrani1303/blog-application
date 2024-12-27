from django.urls import path
from . import views

urlpatterns = [
    path('employee/add/', views.add_employee, name='add_employee'),
    path('employee/list/', views.employee_list, name='employee_list'),
    path('employee/delete/<int:empid>/', views.delete_employee, name='delete_employee'),
    path('employee/update/<int:empid>/', views.update_employee, name='update_employee'),
]

