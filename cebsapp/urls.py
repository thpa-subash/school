from django.urls import path
from . import views

urlpatterns = [



    path('mailcompose/',views.compose),
    path('inbox/',views.inbox),
#//path('inbox/', cebsapp.views.inbox,name="tdetails"),

]