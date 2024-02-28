from django.http import HttpResponse
from .models import *
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('hello')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'exam/login.html')   



# Create your views here.
@csrf_exempt
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
    
class CourseTableView(CreateView):
    model = Course
    fields = "__all__"

    def get_success_url(self):
        return reverse('Course')


