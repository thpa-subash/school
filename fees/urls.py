from django.urls import path


from .import views


urlpatterns = [

    path('classfee/', views.classfee, name="classfee"),


]