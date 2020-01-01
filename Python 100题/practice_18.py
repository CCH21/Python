import datetime
import time

print('当前日期：', datetime.date.today())
print('当前时间：', time.strftime('%H:%M:%S', time.localtime()))
