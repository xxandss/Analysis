#对数据集中的3个csv文件进行聚合，生成一个csv，
#包含电影的信息，其中每部电影一行，信息包括电影名称、主演、平均分、所有tag
#读取文件
import pandas as pd
from pandas.core.frame import DataFrame
file1 = open('E:/技术培训/3 数据分析基础/2 pandas基本变换/pandas2.2/file/links.csv',encoding='utf-8')
file2 = open('E:/技术培训/3 数据分析基础/2 pandas基本变换/pandas2.2/file/movies.csv',encoding='utf-8')
file3 = open('E:/技术培训/3 数据分析基础/2 pandas基本变换/pandas2.2/file/ratings.csv',encoding='utf-8')
file4 = open('E:/技术培训/3 数据分析基础/2 pandas基本变换/pandas2.2/file/tags.csv',encoding='utf-8')

links = pd.read_csv(file1)
movies = pd.read_csv(file2)
ratings = pd.read_csv(file3)
tags = pd.read_csv(file4)

#电影名称
movid = DataFrame(movies['movieId'].drop_duplicates().tolist())
movid.columns = ['movieId']  
movie = movies.drop(columns=['genres'])
result1 = pd.merge(movid,movie,how = 'left',on='movieId')

#电影评分
rating = ratings.groupby(['movieId'],as_index=False)['rating'].mean()
result2 = pd.merge(result1,rating,how = 'left',on='movieId')

#电影tags
tagsf = tags.groupby(['movieId'],as_index=False)['tag'].apply(lambda x:x.str.cat(sep=',')).reset_index()
tagsf.columns=['movieId','tags']
result3 = pd.merge(result2,tagsf,how = 'left',on='movieId')

#展示结果
print(result3)