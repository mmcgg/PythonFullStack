# -*- coding: utf-8 -*-

import pymysql
# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE id = '%s' " % ( 1 )
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except Exception as e:
    print(e)
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
