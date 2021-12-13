from django.db import models

from User.models import User

from utils.media_url import get_media_url
from utils.time_str_covert import datetime_to_str


class Music(models.Model):
    """ 音乐
    """
    name = models.CharField(max_length=64, verbose_name='名称', help_text='名称')
    music_file = models.FileField(upload_to='music', verbose_name='音乐文件', help_text='音乐文件')
    lyrics_file = models.FileField(upload_to='lyrics', verbose_name='歌词文件', help_text='歌词文件')
    cover_image = models.ImageField(upload_to='music_cover', verbose_name='音乐封面', help_text='音乐封面')
    upload_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='上传者', help_text='上传者')

    author = models.CharField(max_length=64, verbose_name='作者', help_text='作者')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')
    music_duration = models.CharField(max_length=16, verbose_name='时长', help_text='时长')

    class Meta:
        verbose_name_plural = '音乐'
        verbose_name = '音乐'

    def __str__(self):
        return self.name

    def out_info(self) -> dict:
        """ 对外信息
        """
        return {
            'id': self.id,
            'music_file': get_media_url(self.music_file.url),
            'lyrics_file': get_media_url(self.lyrics_file.url),
            'cover_image': get_media_url(self.cover_image.url),
            'upload_user': self.upload_user.nickname,

            'author': self.author,

            'create_time': datetime_to_str(self.create_time),
            'music_duration': self.music_duration,
        }
