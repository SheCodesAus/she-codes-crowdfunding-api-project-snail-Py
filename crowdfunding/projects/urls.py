from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('tag/', views.TagList.as_view(), name='tag-list'),
    path('tag/<slug:slug>/', views.TagDetail.as_view(), name='tag-detail'),
    path('faq/<int:pk>', views.FaqDetail.as_view()),
    path('faq/', views.FaqList.as_view()),
    path('milestone/', views.MilestoneList.as_view()),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)