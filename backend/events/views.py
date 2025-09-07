from rest_framework import generics
from .models import College
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Avg
from django.db import models
from .models import College, Student, Event, Registration, Attendance, Feedback
from .serializers import (
    CollegeSerializer, StudentSerializer, EventSerializer,
    RegistrationSerializer, AttendanceSerializer, FeedbackSerializer

)

# CRUD APIs
class CollegeListCreateView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RegistrationListCreate(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class AttendanceListCreate(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class FeedbackListCreate(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


# 1. Event Popularity Report
@api_view(["GET"])
def event_popularity(request):
    events = Event.objects.annotate(reg_count=Count("registration")).order_by("-reg_count")
    data = [
        {
            "event": e.name,
            "registrations": e.reg_count,
            "college": e.college.name,
            "event_type": e.event_type,
        }
        for e in events
    ]
    return Response(data)

# 2. Student Participation Report
@api_view(["GET"])
def student_participation(request):
    students = Student.objects.annotate(attended=Count("attendance", filter=models.Q(attendance__present=True)))
    data = [
        {
            "student": s.name,
            "email": s.email,
            "college": s.college.name,
            "events_attended": s.attended,
        }
        for s in students
    ]
    return Response(data)

# 3. Top 3 Most Active Students
@api_view(["GET"])
def top_students(request):
    students = Student.objects.annotate(attended=Count("attendance", filter=models.Q(attendance__present=True))).order_by("-attended")[:3]
    data = [
        {
            "student": s.name,
            "college": s.college.name,
            "events_attended": s.attended,
        }
        for s in students
    ]
    return Response(data)

# 4. Average Feedback per Event
@api_view(["GET"])
def event_feedback(request):
    events = Event.objects.annotate(avg_rating=Avg("feedback__rating"))
    data = [
        {
            "event": e.name,
            "average_feedback": round(e.avg_rating or 0, 2),
        }
        for e in events
    ]
    return Response(data)