from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Department(models.Model):
    title = models.CharField(max_length=50)
    h_o_d = models.OneToOneField(
        "Staff", related_name="h_o_d", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Department_member(models.Model):
    department = models.ForeignKey(
        "Department", related_name="members", on_delete=models.CASCADE)
    member = models.ForeignKey(
        "Staff", related_name="department", on_delete=models.CASCADE)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.member} {self.position}"


class Subject(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='Staffs/images', max_length=100)
    message = models.TextField()
    subject_one = models.ForeignKey(
        "Subject", related_name="subject_one", blank=True, null=True, on_delete=models.CASCADE)
    subject_two = models.ForeignKey(
        "Subject", related_name="subject_two", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Stream(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Class(models.Model):
    lvl_choices = {
        ('form 1', "form 1"),
        ('form 2', "form 2"),
        ('form 3', "form 3"),
        ('form 4', "form 4"),
    }
    level = models.CharField(max_length=20, choices=lvl_choices)
    stream = models.ForeignKey("Stream", on_delete=models.CASCADE)
    teacher = models.OneToOneField("Staff", on_delete=models.CASCADE, blank=True, null=True)
    prefect = models.OneToOneField("Student", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.level} {self.stream}"

    class Meta:
        verbose_name_plural = "Classes"


class Student(models.Model):
    adm_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    class_level = models.ForeignKey(
        "Class", related_name="students", on_delete=models.CASCADE)
    image = models.FileField(upload_to="students/images")

    def __str__(self):
        return self.name


class Student_leadership(models.Model):
    position = models.CharField(max_length=100)
    student = models.ForeignKey(
        "Student", related_name="roles", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.position}: {self.student}"


class Dorm(models.Model):
    title = models.CharField(max_length=50)
    captain = models.ForeignKey(
        "Student", related_name="captain", on_delete=models.CASCADE)
    dep_captain = models.ForeignKey("Student", on_delete=models.CASCADE)
    motto = models.TextField()
    master = models.OneToOneField("Staff",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} motto: {self.motto}"


class Club(models.Model):
    title = models.CharField(max_length=100)
    aims = models.TextField()
    message = models.TextField()
    president = models.OneToOneField("Student", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
