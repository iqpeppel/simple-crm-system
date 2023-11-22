import math
from math import sqrt
import sqlite3

def connect(sql):
    global results
    # connect = pymysql.connect(
    #     host='127.0.0.1',  # 连接主机, 默认127.0.0.1
    #     user='root',  # 用户名
    #     passwd='123mysql',  # 密码
    #     port=3306,  # 端口，默认为3306
    #     db='crm',  # 数据库名称
    #     charset='utf8'  # 字符编码
    # )
    connect=sqlite3.connect('./database/db-source/crm.sqlite3')
    cursor = connect.cursor()   #使用cursor()获取游标
    cursor.execute(sql)     #执行sql语句
    results = cursor.fetchall() #拿到结果
    results = list(results)
    connect.commit()
    cursor.close()
    connect.close()
    return results
data=connect("SELECT fname,fid,fcid, fprice FROM food")
data = [[row[0], int(row[1]), float(row[2]), float(row[3])] for row in data]

# print(data)
def tuijian(class_id, price):
    price = float(price)
    max_value_col1 = max(i[2] for i in data)
    min_value_col1 = min(i[2] for i in data)
    max_value_col2 = max(i[3] for i in data)
    min_value_col2 = min(i[3] for i in data)
    class_id_distance = max_value_col1 - min_value_col1
    price_distance = max_value_col2 - min_value_col2
    result_list = []
    # print(class_id_distance)
    # print(price_distance)
    for i in data:
        result = sqrt(((class_id - i[2])/ class_id_distance) ** 2 + ((price - i[3])/ price_distance) ** 2)
        result_list.append(result)
    
    
    new_list = [[i[0], i[1],i[3]] for i in data]
    for i in range(len(data)):
        new_list[i].append(result_list[i])
    
    new_list.sort(key=lambda x: x[3])
    #print(new_list)
    return(new_list)

if __name__ == "__main__":
    class_id = 70
    price = 60
    result = tuijian(class_id, price)
    print(result)
