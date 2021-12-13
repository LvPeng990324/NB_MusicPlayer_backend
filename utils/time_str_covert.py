# 时间/日期和字符串转换相关
import datetime


def datetime_to_str(datetime_: datetime.datetime) -> str:
    """ 时间转字符串
    """
    return datetime_.strftime('%Y-%m-%d %H:%M:%S')


