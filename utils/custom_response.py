# 自定义响应
from django.http import JsonResponse


def response_200(message, data=None):
    return JsonResponse(data={
        'code': 200,
        'message': message,
        'data': data,
    })


def response_404(message, data=None):
    return JsonResponse(data={
        'code': 404,
        'message': message,
        'data': data,
    })



