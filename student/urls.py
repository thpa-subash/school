from django.urls import path
from .import views


urlpatterns = [

    path('newstudent/', views.newstd, name="NewStudent"),
    path('approve/', views.approve, name="NewStudent"),
    path('delete/', views.approve, name="NewStudent"),
    path('eg/', views.example, name="example"),



]