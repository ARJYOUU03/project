from django.db import models

# Create your models here.
class Exam(models.Model):
    exam_id=models.IntegerField()
    sem=models.IntegerField()
    year=models.IntegerField()
    month=models.CharField(max_length=20)
    grad_level=models.CharField(max_length=20)

    def __str__(self):
        return self.grad_level

class Department(models.Model):
    dept_id = models.IntegerField()
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name


class Programme(models.Model):
    pgm_id = models.IntegerField(unique=True)
    pgm_name = models.CharField(max_length=50)
    grad_level = models.ForeignKey(Exam,on_delete=models.CASCADE)
    dept_id = models.ForeignKey(Department,on_delete=models.CASCADE)

class Course(models.Model):
    course_id = models.IntegerField()
    course_title = models.CharField(max_length=50)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    Syllabus_year = models.IntegerField() 

class ExamTimeTable(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    date=models.DateField()
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    course_id = models.ForeignKey(Course,models.CASCADE)


    