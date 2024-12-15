import pandas as pd
from numpy.core.defchararray import title
# 导入配置
from pyecharts import options as opts
# 导入柱状体
from pyecharts.charts import Bar, Pie,Line
from scipy.spatial.distance import cityblock
from sqlalchemy.engine import cursor
# from scipy.special import title
from sqlalchemy.orm import Session
from sympy.benchmarks.bench_discrete_log import data_set_1

from sql.sql import engine, DataInfo,DataInfo1, DataInfo2


# 实现数据读取和分析
def get_data():
    #  查询sql里面的数据
    #  通过session去查询
    session = Session(engine)
    #  查询全部的数据
    sql_all = session.query(DataInfo).all()
    data = {
        'year': [],
        'income': [],
        'expend':[],
        'income_rate':[],
        'expend_rate':[]
    }
    print(sql_all)
    for item in sql_all:
        # 将数据处理成字典  x == 年份  y == 数量
        data['year'].append(item.year)
        data['income'].append(item.income)
        data['expend'].append(item.expend)
        data['income_rate'].append(item.income_rate)
        data['expend_rate'].append(item.expend_rate)
    print(data)
    # 返回数据结构以供数据可视化
    return data

def get_city_data():
    #  查询sql里面的数据
    #  通过session去查询
    session = Session(engine)
    #  查询全部的数据
    sql_all = session.query(DataInfo1).all()
    data1 = {
        'year': [],
        'city_income': [],
        'city_expend':[],
        'city_income_rate':[],
        'city_expend_rate':[]
    }
    print(sql_all)
    for item in sql_all:
        # 将数据处理成字典  x == 年份  y == 数量
        data1['year'].append(item.year)
        data1['city_income'].append(item.city_income)
        data1['city_expend'].append(item.city_expend)
        data1['city_income_rate'].append(item.city_income_rate)
        data1['city_expend_rate'].append(item.city_expend_rate)
    print(data1)
    # 返回数据结构以供数据可视化
    return data1
def get_countryside_data():
    #  查询sql里面的数据
    #  通过session去查询
    session = Session(engine)
    #  查询全部的数据
    sql_all = session.query(DataInfo2).all()
    data2 = {
        'year': [],
        'countryside_income': [],
        'countryside_expend':[],
        'countryside_income_rate':[],
        'countryside_expend_rate':[]
    }
    print(sql_all)
    for item in sql_all:
        # 将数据处理成字典  x == 年份  y == 数量
        data2['year'].append(item.year)
        data2['countryside_income'].append(item.countryside_income)
        data2['countryside_expend'].append(item.countryside_expend)
        data2['countryside_income_rate'].append(item.countryside_income_rate)
        data2['countryside_expend_rate'].append(item.countryside_expend_rate)
    print(data2)
    # 返回数据结构以供数据可视化
    return data2


# 渲染柱状体
def dataBar():
    # 获取可视化的数据
    data = get_data()
    data1= get_city_data()
    data2= get_countryside_data()
    # 实例化对象
    bar = Bar()
    print(bar)
    # 初始化横坐标
    # 年份渲染在x轴上
    bar.add_xaxis(data['year'])
    # 初始化纵坐标
    # 年份对应的数量渲染在y轴上
    bar.add_yaxis(
        '全国居民人均可支配收入',
        data['income'],
        label_opts=opts.LabelOpts(is_show=True, position="top",color="#000000"),  # 可选：显示标签并设置颜色
        itemstyle_opts=opts.ItemStyleOpts(color="#FF6347"),  # 柱子颜色
        bar_width=10
    )
    bar.add_yaxis(
        '全国居民人均消费支出',
        data['expend'],
        label_opts=opts.LabelOpts(is_show=True, position="top", color="#000000"),
        bar_width=10)
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="全国居民人均可支配收入与消费支出对比", subtitle="数据来源：国家统计局",
                                  pos_left="center", pos_top="20px"))

    # 生成图形化文件, 文件格式以.html
    bar.render(path='../html/bar.html')

def dataLine():
    data = get_data()
    data1 = get_city_data()
    data1= get_city_data()
    data2= get_countryside_data()
    # 实例化对象
    line = Line()
    print(line)
    # 初始化横坐标
    # 年份渲染在x轴上
    line.add_xaxis(data['year'])
    # 初始化纵坐标
    # 年份对应的数量渲染在y轴上
    line.add_yaxis(
        '全国居民人均可支配收入比上年增长',
        data['income_rate'],
        label_opts=opts.LabelOpts(is_show=True, position="top",color="#000000"),  # 可选：显示标签并设置颜色
        itemstyle_opts=opts.ItemStyleOpts(color="#FF6347"),  # 柱子颜色

    )
    line.add_yaxis(
        '全国居民人均消费支出比上年增长',
        data['expend_rate'],
        label_opts=opts.LabelOpts(is_show=True, position="bottom", color="#000000"),
    )
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="全国居民人均可支配收入与消费支出比上年增长对比", subtitle="数据来源：国家统计局",
                                  pos_left="center", pos_top="20px"))

    # 生成图形化文件, 文件格式以.html
    line.render(path='../html/line.html')

def dataPie():
    data1 = get_city_data()
    data2 = get_countryside_data()

    # 取最后一个数据作为代表
    city_last_rate = data1['city_income_rate'][-1]
    countryside_last_rate = data2['countryside_income_rate'][-1]

    # 构建用于饼图的数据对
    pairs = [
        ("城镇人均收入比例", city_last_rate),
        ("农村人均收入比例", countryside_last_rate)
    ]

    pie = Pie()
    # 添加数据到饼图
    pie.add("", pairs)  # 第一个参数留空，表示不为这些数据指定一个统一的分类名称
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="2021年城镇居民与农村居民人均收入比例对比",
                                  subtitle="数据来源：国家统计局",
                                  pos_left="center", pos_top="20px")
    )
    pie.render('../html/pie.html')

def dataPie1():
        data1 = get_city_data()
        data2 = get_countryside_data()

        # 取最后一个数据作为代表
        city_last_rate = data1['city_expend_rate'][-1]
        countryside_last_rate = data2['countryside_expend_rate'][-1]

        # 构建用于饼图的数据对
        pairs = [
            ("城镇人均支出比例", city_last_rate),
            ("农村人均支出比例", countryside_last_rate)
        ]

        pie = Pie()
        # 添加数据到饼图
        pie.add("", pairs)  # 第一个参数留空，表示不为这些数据指定一个统一的分类名称
        pie.set_global_opts(
            title_opts=opts.TitleOpts(title="2021年城镇居民与农村居民人均支出比例对比",
                                      subtitle="数据来源：国家统计局",
                                      pos_left="center", pos_top="20px")
        )
        pie.render('../html/pie1.html')



if __name__ == '__main__':
    # 渲染
    dataBar()
    dataLine()
    dataPie()
    dataPie1()
