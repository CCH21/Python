#!/usr/bin/env python3

import time
from multiprocessing.dummy import Pool


#################################################
# # 单线程串行方式
# def get_page(string):
#     print('正在下载：', string)
#     time.sleep(2)
#     print('下载成功：', string)
#
#
# name_list = ['aa', 'bb', 'cc', 'dd']
#
# start_time = time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
# print('%ds' % (end_time - start_time))

#################################################

# 线程池方式
start_time = time.time()


def get_page(string):
    print('正在下载：', string)
    time.sleep(2)
    print('下载成功：', string)


name_list = ['aa', 'bb', 'cc', 'dd']

# 实例化一个线程池对象
pool = Pool(4)
# 将列表中每一个列表元素传递给get_page进行处理
pool.map(get_page, name_list)

end_time = time.time()
print(str(end_time - start_time) + 's')

#################################################
