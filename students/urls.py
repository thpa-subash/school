from django.urls import path


from .import views


urlpatterns = [

    path('add_student/',views.add_student, name="add_student"),
    path('student_details/<int:id>', views.student_details, name="student_details"),
    path('edit_student/<int:id>', views.edit_student, name="edit_student"),
    path('newstudent/', views.newstd, name="NewStudent"),
    path('approve/', views.approve, name="NewStudent"),
    path('delete_student/<int:id>', views.delete_student, name="NewStudent"),
    path('update_student/<int:id>', views.update_student, name="update"),
    path('update_fee/<int:id>', views.update_fee, name="update_fee"),
    path('studentfees/',views.studetsearchfees,name="studentFees"),
    path('fees/<int:id>',views.fees,name="Fees"),
    path('studentfeeupdate',views.studentfeeupdate,name="studentfeeupdate"),
    path('deletefeelist/',views.deletefeelist,name="deletefeelist"),
    path('feelist/',views.feelist,name="feelist"),
    path('search/',views.search,name='search'),
]