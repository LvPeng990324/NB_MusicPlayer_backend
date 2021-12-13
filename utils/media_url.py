# 文件访问URL相关
from NB_MusicPlayer_backend.deploy_conf import DEPLOY_URL


def get_media_url(media_path):
    """ 获取文件访问URL
    """
    return DEPLOY_URL + media_path

