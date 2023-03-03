from django.db import models
from django.urls import reverse_lazy
from mptt.models import MPTTModel, TreeForeignKey


class SkillTree(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'дерево навыков'
        verbose_name_plural = 'деревья навыков'

    def __str__(self):
        return self.name

    def get_root_skills(self):
        return self.skills.filter(parent=None)

    def get_absolute_url(self):
        return reverse_lazy('skills:skill-tree-detail', args=[self.pk])


class Skill(MPTTModel):
    name = models.CharField('название', max_length=255)
    skill_tree = models.ForeignKey(SkillTree, verbose_name='дерево', on_delete=models.SET_NULL, null=True, blank=True, related_name='skills') # noqa ignore
    parent = TreeForeignKey('self', verbose_name='род. навык', on_delete=models.CASCADE, null=True, blank=True, related_name='children') # noqa ignore

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'

    def __str__(self):
        return f'[{self.skill_tree.name}] -> {"".join([f"/{ ancestor.name }" for ancestor in self.get_ancestors(include_self=True)])}'

    def get_absolute_url(self):
        return reverse_lazy('skills:skill-detail', args=[self.pk])


class SkillPoint(models.Model):
    skill = models.ForeignKey(Skill, verbose_name='навык', on_delete=models.CASCADE, related_name='points') # noqa ignore
    order = models.IntegerField('порядковый номер')
    title = models.CharField('заголовок', max_length=255)
    description = models.TextField('описание')

    class Meta:
        verbose_name = 'балл навыка'
        verbose_name_plural = 'баллы навыков'

    def __str__(self):
        return f'{self.skill} -> {self.order}.{self.title}'
