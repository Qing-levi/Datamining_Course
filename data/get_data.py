# 爬取数据
# 向服务器发送请求
import requests
# 处理请求日志
import logging
# 对数据进行处理
import pandas as pd
import time

# 函数
# 实现爬取数据的函数

'''
爬数据函数
'''


def get_data(start_time, end_time, income, income_rate, expend, expend_rate, list_name1, list_name2, list_name3, list_name4):
    # 函数体 实现采集数据的功能

    # data_list用于储存爬取的数据
    data_list = []
    # 通过循环实现爬取多个年份的数据
    for key in range(start_time, end_time):
        # 暂缓程序执行
        time.sleep(2)
        # 定义数据采集的目标地址
        url = 'https://data.stats.gov.cn/search.htm'
        # 定义请求参数
        #全国数据
        income_arge = {
            's': str(key) + income,
            "m": "searchdata",
            "db": "",
            "p": 0
        }
        income_rate_arge = {
            's': str(key) + income_rate,
            "m": "searchdata",
            "db": "",
            "p": 0
        }
        expend_arge = {
            's': str(key) + expend,
            "m": "searchdata",
            "db": "",
            "p": 0
        }
        expend_rate_arge = {
            's': str(key) + expend_rate,
            "m": "searchdata",
            "db": "",
            "p": 0
        }
        # 设置日志
        logging.captureWarnings(True)
        # 正式起请求采集数据
        # verify 关闭证书
        income_res = requests.get(url, verify=False, params=income_arge)
        income_data = income_res.json()
        income_value = income_data['result'][0]['data'] if 'result' in income_data and len(income_data['result']) > 0 \
            else None
        income_rate_res = requests.get(url, verify=False, params=income_rate_arge)
        income_rate_data = income_rate_res.json()
        income_rate_value = income_rate_data['result'][0]['data'] if 'result' in income_rate_data and len(
            income_rate_data['result']) > 0 else None
        expend_res=requests.get(url, verify=False, params=expend_arge)
        expend_data=expend_res.json()
        expend_value = expend_data['result'][0]['data'] if 'result' in expend_data and len(expend_data['result']) > 0 \
            else None
        expend_rate_res=requests.get(url, verify=False, params=expend_rate_arge)
        expend_rate_data=expend_rate_res.json()
        expend_rate_value = expend_rate_data['result'][0]['data'] if 'result' in expend_rate_data and len(
            expend_rate_data['result']) > 0 else None
        # # 创建自己需要的数据
        # t = (key, data['result'][0]['data'])
        # 把抓取的数据变成数组对象
        # year data 和数据表模型的字断保持一致
        t = {
            'year': key,
            list_name1: income_value,
            list_name2: expend_value,
            list_name3: income_rate_value,
            list_name4: expend_rate_value
        }
        # 把单个数据字典添加到列表中
        # a = [{'year': 2018, 'data': 20}, {'year': 2018, 'data': 20}]
        data_list.append(t)
    # 爬取数据结束后访问
    print(data_list)
    # 把当前的数据返回出去，这样可以在函数外访问
    return data_list

def get_all_data(start_time,end_time):
    '''全国数据'''
    income='居民人均可支配收入'
    income_rate='居民人均可支配收入比上年增长'
    expend='居民人均消费支出'
    expend_rate='居民人均消费支出比上年增长'
    list_name1='income'
    list_name2='expend'
    list_name3='income_rate'
    list_name4='expend_rate'
    print('全国居民人均收入支出数据：')
    return get_data(start_time, end_time, income, income_rate, expend, expend_rate, list_name1, list_name2, list_name3, list_name4)

def get_city_data(start_time,end_time):
    '''城镇数据'''
    income='城镇居民人均可支配收入'
    income_rate='城镇居民人均可支配收入比上年增长'
    expend='城镇居民人均消费支出'
    expend_rate='城镇居民人均消费支出比上年增长'
    list_name1='city_income'
    list_name2='city_expend'
    list_name3='city_income_rate'
    list_name4='city_expend_rate'
    print('城镇居民人均收入支出数据：')
    return get_data(start_time, end_time, income, income_rate, expend, expend_rate,list_name1, list_name2, list_name3, list_name4)

def get_countryside_data(start_time,end_time):
    '''农村数据'''
    income='农村居民人均可支配收入'
    income_rate='农村居民人均可支配收入比上年增长'
    expend='农村居民人均消费支出'
    expend_rate='农村居民人均消费支出比上年增长'
    list_name1='countryside_income'
    list_name2='countryside_expend'
    list_name3='countryside_income_rate'
    list_name4='countryside_expend_rate'
    print('农村居民人均收入支出数据：')
    return get_data(start_time, end_time, income, income_rate, expend, expend_rate, list_name1, list_name2, list_name3, list_name4)

if __name__=='__main__':
    get_all_data(2013,2015)
    get_city_data(2013, 2015)
    get_countryside_data(2013, 2015)