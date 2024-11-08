import time


def _():
    time.sleep(float)

    time.time()  # 返回从 epoch 开始的秒数形式的时间（在所有平台上都是 1970-01-01, 00:00:00 (UTC)）


def format():
    time.localtime(float)
    time.mktime(time.struct_time)

    time.strptime(str, '% A' | ...)
    time.strftime('% A' | ..., time.struct_time)
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
