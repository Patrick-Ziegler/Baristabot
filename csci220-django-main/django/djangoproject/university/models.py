from django.db import models


#    Student
#    Course
#    Room
#    Enrollment




class Room(models.Model):
    number = models.CharField(primary_key=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"<Room Number {self.number}. Capacity: {self.capacity}>"
    
class Course(models.Model):
    number = models.CharField(primary_key=True)
    title = models.TextField()
    room = models.ForeignKey(Room, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Course {self.number} - {self.title} in room {self.room}>"


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    enrollment = models.ManyToManyField(Course)

    def __str__(self):
        return "<Profile id={} name={}>".format(
            self.id, self.name
        )
