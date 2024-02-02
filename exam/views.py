from django.shortcuts import render
from django.http import HttpResponse
from .models import Exam
 
# Create your views here.
def home(request):
    return HttpResponse("<H1 ALIGN='CENTER'>WELCOME</H1>")


def addexam(request):
    if request.method=="POST":
        exam_id=request.POST.get('exam_id')
        sem=request.POST.get('sem')
        year=request.POST.get('year')
        month=request.POST.get('month')
        grad_level=request.POST.get('grad_level')
        exam=Exam(exam_id=exam_id,sem=sem,year=year,month=month,grad_level=grad_level)
        exam.save()
        return HttpResponse('Submitted')
    return render(request,'exam/formexam.html')


