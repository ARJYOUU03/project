from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='hello'),
    path('addexam',views.addexam,name='addexam')
]
