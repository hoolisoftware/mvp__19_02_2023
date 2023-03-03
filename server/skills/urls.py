from django.urls import path

from . import views

app_name = 'skills'

urlpatterns = (
    path('', views.SkillTreeListView.as_view(), name='skill-tree-list'),
    path('trees/', views.SkillTreeListView.as_view(), name='skill-tree-list'),
    path('trees/<int:pk>/', views.SkillTreeDetailView.as_view(), name='skill-tree-detail'), # noqa ignore
    path('trees/skills/<int:pk>/', views.SkillDetailView.as_view(), name='skill-detail'), # noqa ignore
)
