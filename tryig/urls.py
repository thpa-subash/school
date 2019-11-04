from django.urls import path
from .import views


urlpatterns = [

    path('add/', views.emp, name="AddStudent"),
    path('add1/', views.emp, name="AddStudent"),
    path('show/', views.show, name="AddStudent"),
    path('edit/<int:id>', views.edit, name="AddStudent"),
    path('update/<int:id>', views.update, name="AddStudent"),


]