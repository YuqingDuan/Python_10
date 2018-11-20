# 读取MySQL中的数据，进行可视化分析

import numpy
import pymysql
import pandas
import matplotlib.pylab as pyl

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Devilhunter9527', db='dangdang', charset='utf8', use_unicode=True)
sql = "select * from books"
# data[row][column]是二维数组
# >>> data.values[0]
# array([' .NET性能优化', 'http://product.dangdang.com/25321299.html', '3条评论'], dtype=object)
data = pandas.read_sql(sql, conn)
# 将得到的数据进行转置处理
data_t = data.T
x = data_t.values[0]
y = data_t.values[2]
pyl.plot(x, y)
pyl.show()
