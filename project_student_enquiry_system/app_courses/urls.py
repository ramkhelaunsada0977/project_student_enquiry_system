from django.urls import path
from . import views

urlspatterns =[
    path('List/',views.course_index, name='course-index'),
    path('Edit/',views.course_edit, name='course-edit'),
    path('Show/',views.course_show, name='course-show'),
    path('create/',views.course_create, name='course-create'),
    

]