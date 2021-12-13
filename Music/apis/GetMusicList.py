from django.views import View
from django.core.paginator import Paginator

from Music.models import Music

from utils.custom_response import response_200


class GetMusicList(View):
    """ 获取音乐列表
    """
    def get(self, request):
        """ # 获取音乐列表
        """
        # 获取分页信息
        page_size = int(request.GET.get('page_size', 10))
        page_num = int(request.GET.get('page_num', 1))

        # 取出所有未删除音乐
        musics = Music.objects.filter(
            is_delete=False,  # 要没删除的
        )

        # 根据创建时间排序
        musics = musics.order_by('-create_time')

        # 加入分页
        total_num = musics.count()
        musics_paged = Paginator(musics, page_size)
        musics = musics_paged.page(page_num).object_list

        # 打包音乐数据
        music_info_list = []
        for music in musics:
            music_info_list.append(music.out_info())

        # 返回响应
        return response_200(
            message='获取成功',
            data={
                'music_info_list': music_info_list,
            }
        )

