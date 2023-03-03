from django.views import generic

from . import models


class SkillTreeListView(generic.ListView):
    model = models.SkillTree
    template_name = 'skills/skill-tree-list.django-html'


class SkillTreeDetailView(generic.DetailView):
    model = models.SkillTree
    template_name = 'skills/skill-tree-detail.django-html'


class SkillDetailView(generic.DetailView):
    model = models.Skill
    template_name = 'skills/skill-detail.django-html'