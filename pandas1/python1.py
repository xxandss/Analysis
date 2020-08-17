#读取rates.csv文件，完成：

#1. 将每1分做为一档，电影的评分共分为5档，(0:1], (1,2], (2, 3], (3, 4], (4, 5], 通过pandas包求出每个评分档共有多少部电影

#2. 添加一个comment列，对4分以上的电影标‘推荐’，其他标‘不推荐’，输出到一个comment.csv中

#1
import pandas as pd
file = open('E:/技术培训/3 数据分析基础/1 pandas基本数据操作/python_basic/file/ratings.csv',encoding = 'utf-8')
ratings = pd.read_csv(file)

a = ratings[['movieId','rating']]
a_mov = ratings['movieId']
#查询空值：   df_na = a['rating'].isna()
b = a.groupby(a_mov)['rating'].mean().tolist()

c1,c2,c3,c4,c5 =0,0,0,0,0
for i  in  range(0,len(b)):    
    if   0<b[i]<=1:
         c1=c1+1 
    if   1<b[i]<=2:
         c2=c2+1 
    if   2<b[i]<=3:
         c3=c3+1 
    if   3<b[i]<=4:
         c4=c4+1 
    if   4<b[i]<=5:
         c5=c5+1 
print('(0,1]评分档电影部数',c1)
print('(1,2]评分档电影部数',c2)
print('(2,3]评分档电影部数',c3)
print('(3,4]评分档电影部数',c4)
print('(4,5]评分档电影部数',c5)
    
    
    
#2  
comment=['123']*len(b)
for i  in  range(0,len(b)):    
    if   0<b[i]<=4:
         comment[i]= '不推荐'
    if   4<b[i]   :
         comment[i]= '推荐' 
#print(comment)  

mov_id = list(set(a_mov))
mov_id.sort()

from pandas.core.frame import DataFrame
comment0={"movieId" : mov_id,
          "rating"  : b,
          "comment" : comment} #将列表转换成字典
data=DataFrame(comment0)

data.to_csv('E:/技术培训/3 数据分析基础/1 pandas基本数据操作/python_basic/comment.csv',index=False,encoding = 'utf-8-sig')

 
         
         
         
         
         
         
         
         
         
      