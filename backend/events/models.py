from django.db import models

class College(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPES = [
        ("workshop", "Workshop"),
        ("seminar", "Seminar"),
        ("hackathon", "Hackathon"),
        ("fest", "Fest"),
    ]
    name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    date = models.DateField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
