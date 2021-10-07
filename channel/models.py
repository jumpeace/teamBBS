from django.db import models
from team.models import Team

class Channel(models.Model):
    name = models.CharField(verbose_name='名称', max_length=255)
    team = models.ForeignKey(Team, verbose_name='チーム', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name