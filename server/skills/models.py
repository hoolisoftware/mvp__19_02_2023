from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class SkillTree(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'дерево навыков'
        verbose_name_plural = 'деревья навыков'

    def __str__(self):
        return self.name


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
        return self.name


class SkillPoint(models.Model):
    skill = models.ForeignKey(Skill, verbose_name='навык', on_delete=models.CASCADE) # noqa ignore
    order = models.IntegerField('порядковый номер')
    title = models.CharField('заголовок', max_length=255)
    description = models.TextField('описание')

    class Meta:
        verbose_name = 'балл навыка'
        verbose_name_plural = 'баллы навыков'

    def __str__(self):
        return self.title
