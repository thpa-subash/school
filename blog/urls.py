from django.urls import path


from .import views


urlpatterns = [

    path('createblog/',views.createblog, name="createblog"),
    path('allblogs/', views.allblogs, name="allblog"),
    path('details/<int:id>', views.details, name="blogdetails"),

]
