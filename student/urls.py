from django.urls import path


from .import views


urlpatterns = [

    path('add_student/', views.add_student, name="AddStudent"),
    path('student_details/', views.student_details, name="studentdetails"),
    path('edit_student/<int:id>', views.edit_student, name="editstudent"),
    path('newstudent/', views.newstd, name="NewStudent"),
    path('approve/', views.approve, name="NewStudent"),
    path('delete/<int:id>', views.delete_student, name="NewStudent"),
    path('update/<int:id>', views.update, name="update"),
]