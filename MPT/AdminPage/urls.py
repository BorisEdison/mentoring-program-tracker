from django.urls import path
from . import views


urlpatterns = [
    # this is for student dashboard
   
    # this is for admin page
    path('', views.Adminpage, name= 'admin'),
    path('student', views.Adminstudent, name= 'admin-student'),
    path('mentor', views.Adminmentor, name= 'admin-mentor'),
    path('activity', views.Activity, name= 'admin-activity'),
    path('delete/<str:id>/',views.deleteuser, name= 'delete-user'),
    path('update/<str:usr_id>/',views.updateuserprofile, name= 'update-user'),
    path('assigned/<str:usr_id>', views.Assigned, name= 'admin-assigned'),
    path('unassigned/<str:usr_id>', views.Unassigned, name= 'admin-unassigned'),
    ]
