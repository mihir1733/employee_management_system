from django.contrib import admin
from django.urls import path,include
from employee_register.models import Employee,Position
from employee_register import views

urlpatterns = [
   path('',views.employee_form,name='employee_insert'), #get and post request for insert operations
   path('<int:id>/',views.employee_form,name='employee_update'), #get and post request for update operations
   path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
   path('list/',views.employee_list,name='employee_list'), #get request to retrive and display all records
]