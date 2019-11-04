from django.urls import path


from .import views


urlpatterns = [

    path('classfee/', views.classfees, name="classfee"),


]