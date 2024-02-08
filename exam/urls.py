from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='hello'),
    path('exam',views.ExamView.as_view(),name='exam'),
    path('timetable',views.ExamTimeTableView.as_view(),name='timetable'),
    path('duty',views.dutyAllotmentView.as_view(),name='dutyAllotment'),
    path('prefer',views.preferTableView.as_view(),name='preferTable')
]
