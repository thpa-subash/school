from django.urls import path


from .import views


urlpatterns = [

    path('compose/', views.compose, name="Compose"),
    path('inbox/', views.inbox, name="Inbox"),
    path('get_data/', views.getData, name="GET CHART"),

]