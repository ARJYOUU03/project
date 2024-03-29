# Generated by Django 5.0.2 on 2024-02-07 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dept_id", models.IntegerField()),
                ("dept_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("exam_id", models.IntegerField()),
                ("sem", models.IntegerField()),
                ("year", models.IntegerField()),
                ("month", models.CharField(max_length=20)),
                ("grad_level", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_id", models.IntegerField()),
                ("course_title", models.CharField(max_length=50)),
                ("Syllabus_year", models.IntegerField()),
                ("course_code", models.IntegerField()),
                (
                    "dept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exam.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExamTimeTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("time_from", models.DateTimeField()),
                ("time_to", models.DateTimeField()),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.course"
                    ),
                ),
                (
                    "dept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exam.department",
                    ),
                ),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.exam"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Programme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pgm_id", models.IntegerField(unique=True)),
                ("pgm_name", models.CharField(max_length=50)),
                (
                    "dept_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exam.department",
                    ),
                ),
                (
                    "grad_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.exam"
                    ),
                ),
            ],
        ),
    ]
