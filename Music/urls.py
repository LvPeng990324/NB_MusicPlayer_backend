from django.urls import path

from Music.apis.GetMusicList import GetMusicList


app_name = 'Music'

urlpatterns = [
    # 获取音乐列表
    path('get-music-list/', GetMusicList.as_view(), name='get_music_list'),
]
