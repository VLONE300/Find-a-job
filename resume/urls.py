from django.urls import path
from resume.views import ResumeView, ResumeListView, AddResumeView, EditResumeView, DeleteResumeView

urlpatterns = [
    path('resumes/', ResumeListView.as_view(), name='resume-list'),
    path('resume/<int:pk>/', ResumeView.as_view(), name='resume-detail'),
    path('resume/create', AddResumeView.as_view(), name='create-resume'),
    path('resume/<int:pk>/edit/', EditResumeView.as_view(), name='edit-resume'),
    path('resume/<int:pk>/delete/', DeleteResumeView.as_view(), name='delete-resume'),

]
