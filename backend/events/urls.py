from django.urls import path
from .views import (
    CollegeListCreateView,
    StudentListCreate,
    EventListCreate,
    RegistrationListCreate,
    AttendanceListCreate,
    FeedbackListCreate,
    event_popularity,
    student_participation,
    top_students,
    event_feedback,
)

urlpatterns = [
    path("colleges/", CollegeListCreateView.as_view()),
    path("students/", StudentListCreate.as_view()),
    path("events/", EventListCreate.as_view()),
    path("registrations/", RegistrationListCreate.as_view()),
    path("attendance/", AttendanceListCreate.as_view()),
    path("feedback/", FeedbackListCreate.as_view()),

    # Reports
    path("reports/event-popularity/", event_popularity),
    path("reports/student-participation/", student_participation),
    path("reports/top-students/", top_students),
    path("reports/event-feedback/", event_feedback, name="event-feedback"),
]

