from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Department_member)
admin.site.register(Student)
admin.site.register(Student_leadership)
admin.site.register(Class)
admin.site.register(Stream)
admin.site.register(Club)
admin.site.register(Dorm)

