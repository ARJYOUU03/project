from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='hello'),
    path('addexam',views.addexam,name='addexam'),
    path('timetable',views.ExamTimeTableView.as_view(),name='timetable')
]
