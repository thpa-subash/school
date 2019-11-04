from django.urls import path


from .import views


urlpatterns = [

    path('add_teacher/', views.add_teacher, name="Addteacher"),
    path('teacher_details/', views.teacher_details, name="teacherdetails"),
    path('edit_teacher/<int:id>', views.edit_teacher, name="editteacher"),

    path('approve/', views.approve, name="approveteacher"),
    path('search/', views.search, name="search"),
    path('delete/<int:id>', views.delete, name="deleteteacher"),
    path('update/<int:id>', views.update, name="updateteacher"),
]