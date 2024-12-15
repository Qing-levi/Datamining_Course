# 导入相关函数
import os

import sqlalchemy
from pyarrow import string
from sqlalchemy import create_engine, Column, String, Float, Integer,Double
from sqlalchemy.orm import declarative_base, Session
from data.get_data import get_all_data,get_city_data,get_countryside_data

# 创建数据库链接
# root 为默认登录账号
# Wz987464 登录密码
# localhost 本地网络
# app 数据库
DATABASE_URL = 'mysql+pymysql://root:Lihan0905@localhost/app'

#  创建数据库引擎， 进行数据库的链接
#  DATABASE_URL 数据库配置
engine = create_engine(DATABASE_URL)
# 创建Session对象， 便于对mysql进行增  删， 改， 查
# engine 数据库引擎
session = Session(engine)
# 创建基类  所有的数据表继承基类
Base = declarative_base()


# 创建数据表模型

class DataInfo(Base):
    # 数据表的名称
    # __tablename__ 表示设置数据表的名称，如果没有这个字断则会以class名作为表名
    __tablename__ = '全国居民收入与支出情况',

    #  Integer 表示id字断为整数
    #  primary_key 为唯一数据标记， 没来标记每一条数据
    # autoincrement 设置标记为自增类型   1， 2， 3 。。。。。。
    id = Column(Integer, primary_key=True, autoincrement=True)
    #  year 年份
    #  String 表为year字断字符串
    year = Column(String(128))
    #  data 表示year对应的数量
    #  Float 表示数据类型为浮点
    income = Column(Float)
    expend= Column(Float)
    income_rate= Column(Float)
    expend_rate= Column(Float)


# 创建定义好的数据表
#  engine 创建到对应的数据库
DataInfo.metadata.create_all(engine)

# 创建数据表模型

class DataInfo1(Base):
    # 数据表的名称
    # __tablename__ 表示设置数据表的名称，如果没有这个字断则会以class名作为表名
    __tablename__ = '城镇居民收入与支出情况',

    #  Integer 表示id字断为整数
    #  primary_key 为唯一数据标记， 没来标记每一条数据
    # autoincrement 设置标记为自增类型   1， 2， 3 。。。。。。
    id = Column(Integer, primary_key=True, autoincrement=True)
    #  year 年份
    #  String 表为year字断字符串
    year = Column(String(128))
    #  data 表示year对应的数量
    #  Float 表示数据类型为浮点
    city_income = Column(Float)
    city_expend= Column(Float)
    city_income_rate= Column(Float)
    city_expend_rate= Column(Float)

# 创建定义好的数据表
#  engine 创建到对应的数据库
DataInfo1.metadata.create_all(engine)
# 创建数据表模型

class DataInfo2(Base):
    # 数据表的名称
    # __tablename__ 表示设置数据表的名称，如果没有这个字断则会以class名作为表名
    __tablename__ = '农村居民收入与支出情况',

    #  Integer 表示id字断为整数
    #  primary_key 为唯一数据标记， 没来标记每一条数据
    # autoincrement 设置标记为自增类型   1， 2， 3 。。。。。。
    id = Column(Integer, primary_key=True, autoincrement=True)
    #  year 年份
    #  String 表为year字断字符串
    year = Column(String(128))
    #  data 表示year对应的数量
    #  Float 表示数据类型为浮点
    countryside_income = Column(Float)
    countryside_expend= Column(Float)
    countryside_income_rate= Column(Float)
    countryside_expend_rate= Column(Float)

# 创建定义好的数据表
#  engine 创建到对应的数据库
DataInfo2.metadata.create_all(engine)

#  把数据写入数据库
def set_sql():
    #  得到脚本爬取的数据
    data1 = get_all_data(2012, 2022)
    data2=get_city_data(2012,2022)
    data3=get_countryside_data(2012,2022)
    print(data1,data2,data3)
    #  把数据写入到数据库
    #  第一个参数表示数据模型
    #  第二个参数表示写入的数据data  [{'year': 2018, 'data': 20}, {'year': 2018, 'data': 20}]
    session.bulk_insert_mappings(DataInfo, data1)
    session.bulk_insert_mappings(DataInfo1, data2)
    session.bulk_insert_mappings(DataInfo2, data3)
    #  提交sql里面  commit才把数据添加的到数据表
    session.commit()



if __name__ == '__main__':
    set_sql()
