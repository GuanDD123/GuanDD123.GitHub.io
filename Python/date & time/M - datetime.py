import datetime
from datetime import date as Date, datetime as Datetime


def format(date_datetime: Date | Datetime):
    Date.fromtimestamp(float)
    Datetime.fromtimestamp(timestamp=float)

    Datetime.strptime(str, '% A' | ...)
    date_datetime.strftime(format='% A' | ...)
    '''设置日期和时间格式的实参
    %A：星期几（Monday ~ Sunday）
    %B：月份名（January ~ December）
    %m：用数表示的月份（01 ~ 12）
    %d：用数表示的月份中的一天（01 ~ 31）
    %Y：四位的年份（2019 ...）
    %y：两位的年份（19 ...）
    %H：24小时制的小时数（00 ~ 23）
    %I：12小时制的小时数（01 ~ 12）
    %p：am或pm
    %M：分钟数（00 ~ 59）
    %S：秒数（00 ~ 59）
    '''


def get_date(datetime_: Datetime):
    Date.today()
    datetime_.date()

    datetime.timedelta(days=float)  # 返回日期差值
