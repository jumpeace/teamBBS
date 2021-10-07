from django.db import models

from role.models import Role
from team.models import Team
from user.models import User

class User_Team(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, verbose_name='チーム', on_delete=models.CASCADE)
    is_owner = models.BooleanField(verbose_name='オーナーかどうか',default=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return f'{self.user}-{self.team}'


class User_Role(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name='役職', on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return f'{self.user}-{self.role}'
