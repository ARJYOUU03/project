from django.shortcuts import render
from django.http import HttpResponse
from .models import Exam,ExamTimeTable,teacherTable,dutyAllotment,preferTable
from django.views.generic.edit import CreateView
from django.urls import reverse
 
# Create your views here.
def home(request):
    return render(request,'exam/home.html')


class ExamView(CreateView):
    model = Exam
    fields = "__all__"

    def get_success_url(self):
        return reverse('Exam')


class ExamTimeTableView(CreateView):
    model = ExamTimeTable
    fields = "__all__"

    def get_success_url(self):
        return reverse('ExamTimeTable')
    

class teacherTableView(CreateView):
    model = teacherTable
    fields = "__all__"

    def get_success_url(self):
        return reverse('teacherTable')
    
class dutyAllotmentView(CreateView):
    model = dutyAllotment
    fields = "__all__"

    def get_success_url(self):
        return reverse('dutyAllotment')
    
class preferTableView(CreateView):
    model = preferTable
    fields = "__all__"

    def get_success_url(self):
        return reverse('preferTable')