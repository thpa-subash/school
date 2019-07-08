from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('newstudent/', views.new, name="New Student"),

]
