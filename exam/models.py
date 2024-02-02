from django.db import models

# Create your models here.
class Exam(models.Model):
    exam_id=models.IntegerField()
    sem=models.IntegerField()
    year=models.IntegerField()
    month=models.CharField(max_length=20)
    grad_level=models.CharField(max_length=20)
    