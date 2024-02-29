from django.urls import path
from . import views

urlpatterns = [
    path('',views.mylogin,name='login'),
    path('home/',views.home,name='hello'),
    path('exam/',views.ExamView.as_view(),name='exam'),
    path('timetable/',views.ExamTimeTableView.as_view(),name='timetable'),
    path('duty/',views.dutyAllotmentView.as_view(),name='dutyAllotment'),
    path('prefer/',views.preferTableView.as_view(),name='preferTable'),
    path('course/',views.CourseTableView.as_view(),name='course'),
    path('cpage/',views.cheifpage,name='cpage')
]

