import pandas as pd
file = open('E:/技术培训/3 数据分析基础/3 时序处理/login_data.csv','r')
login_data = pd.read_csv(file)
login_data
# 时序处理技术练习
#基于时间进行数据分析是进行数据分析常见的场景。比如，我们要按月分析贷款逾期率，按天分析用户流失率。这些关于时间的分析都离不开一个强大的时序处理工具。
#有一组用户登录的数据`login_data.csv`，格式如下：
#
#   |  login_at  | id |
#   | :--: | :--: |
#   | 2020-07-01 12:00:00  | 1 |
#   | 2020-07-02 12:00:00  | 2 |
#
#请使用`pandas`读取此数据，进行分析。实现：
#
#1. 创建一列，根据国内的法定假期规定，从登录时间确定当天是否是工作日。
#2. 统计节假日的平均每日独立登录用户数，工作日的平均每日独立登录用户数。
#1
import datetime
from chinese_calendar import is_workday
a = login_data['login_at']
workday = [123]*len(a)
for i in range(0,len(a)):
    b = datetime.datetime.strptime(a[i],'%Y-%m-%d %H:%M:%S')
    if is_workday(b):
      c = "Y"
    else:
      c = "N"
    workday[i] = c

workday = pd.DataFrame(workday)
login_data['workday'] = workday

#2
data_N = login_data[login_data['workday']=='N'] 
avg_N = sum(data_N['id'])/len(data_N)
print('节假日平均每日独立登录用户数',avg_N)

data_Y = login_data[login_data['workday']=='Y'] 
avg_Y = sum(data_Y['id'])/len(data_Y)
print('工作日平均每日独立登录用户数',avg_Y)


  
  
  
  
  
  
  