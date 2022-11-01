from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('news/',views.news,name="news"),
    path('search/',views.search,name="search"),
    path('active_inactive/',views.active_inactive,name="active_inactive"),
    path('add/',views.add,name="add"),
    path('contact/',views.contact,name="contact"),
    path('<int:stu_id>',views.edit,name="edit"),
    path('show/',views.show,name="show"),
    path('delete/<int:stu_id>',views.delete,name="delete"),
    path('_edit/<int:stu_id>',views._edit,name="_edit"),
    path('onecourse/<str:course_name>',views.onecourse,name="onecourse"),
    #____________________________________________________________________
    path('gpaerror/',views.gpaerror,name="gpaerror"),
    path('level/',views.level,name="level"),
    path('dep/',views.dep,name="dep"),
    path('fine/',views.fine,name="fine"),
    #///////////////////////////////////

   
]
