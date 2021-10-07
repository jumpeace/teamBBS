from django.db import models
from user.models import User
from channel.models import Channel

# class Channel(models.Model):
#     name = models.CharField(verbose_name='名称', max_length=255)
#     team = models.ForeignKey(Team, verbose_name='チーム', on_delete=models.CASCADE, null=True)
#     created_at = models.DateTimeField('作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField('更新日時', auto_now=True)

#     objects = ChannelManager

#     def __str__(self):
#         return self.name


class Post(models.Model):
    channel = models.ForeignKey(Channel, verbose_name='チャンネル', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='内容', max_length=255)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.content
