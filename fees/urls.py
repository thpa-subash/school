from django.urls import path


from .import views


urlpatterns = [

    path('classfees/', views.classfee, name="classfees"),
    path('feedetails/',views.feedetails ,name="feedetails")

]