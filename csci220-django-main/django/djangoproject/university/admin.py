from django.contrib import admin

from .models import Room, Course, Student

admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Student)

# Register your models here.
