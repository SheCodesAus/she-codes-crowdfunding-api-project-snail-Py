from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('tag/<slug:slug>/', views.TagDetail.as_view(), name='tag'),
    path('<int:project_id>/questions/', views.QuestionDetail.as_view()),
    path('<int:project_id>/answers/', views.AnswerDetail.as_view())

    ]

urlpatterns = format_suffix_patterns(urlpatterns)