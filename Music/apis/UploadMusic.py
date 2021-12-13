from django.views import View

from Music.models import Music
from User.models import User


class UploadMusic(View):
    """ 上传音乐
    """
    def post(self, request):
        """ 上传音乐
        """


