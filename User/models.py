from django.db import models

from utils.media_url import get_media_url
from utils.time_str_covert import datetime_to_str


class User(models.Model):
    """ 用户
    """
    nickname = models.CharField(unique=True, max_length=64, verbose_name='昵称', help_text='昵称')
    avatar = models.ImageField(upload_to='avatar', verbose_name='头像', help_text='头像')
    password_md5 = models.CharField(max_length=32, verbose_name='md5后密码', help_text='md5后密码')
    description = models.TextField(default='', verbose_name='介绍', help_text='介绍')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')

    class Meta:
        verbose_name_plural = '用户'
        verbose_name = '用户'

    def __str__(self):
        return self.nickname

    def out_info(self):
        """ 对外信息
        """
        return {
            'id': self.id,
            'nickname': self.nickname,
            'avatar': get_media_url(self.avatar.url),
            'description': self.description,

            'create_time': datetime_to_str(self.create_time),
        }
