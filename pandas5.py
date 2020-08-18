# pandas基本绘图

#可视化统计分析结果可以让我们更直观的发现数据里面隐藏的规律，辅助我们理解数据。pandas提供了非常丰富的绘制图表的能力。
#
#请使用`notebook`编写一段代码，读取`iris.csv`数据集，分析其数据分布情况。
#
#鸢尾花一共可以分为Setosa，Versicolour，Virginica三个种类。`iris`数据集是一个关于鸢尾花的数据集。
#在这个数据集中，一共搜集了花萼长度，花萼宽度，花瓣长度，花瓣宽度4个属性。
#
#请根据你所掌握的pandas绘图知识，绘制下面两张数据分布图：
#
#1. ![花瓣特征与鸢尾花类型分布](petal_width_and_length.png)
#2. ![花萼特征与鸢尾花类型分布](sepal_width_and_length.png)

import pandas as pd
file = open('E:/技术培训/3 数据分析基础/5 基本绘图/数据集/iris.csv',encoding = 'utf-8')
iris = pd.read_csv(file)
#SepalLength	SepalWidth	PetalLength	PetalWidth	

data1 = iris[['SepalLength','SepalWidth','Name']] 
data2 = iris[['PetalLength','PetalWidth','Name']] 
data1_se = data1[data1['Name']=='Iris-setosa']
data1_ve = data1[data1['Name']=='Iris-versicolor']
data1_vi = data1[data1['Name']=='Iris-virginica']
data2_se = data2[data2['Name']=='Iris-setosa']
data2_ve = data2[data2['Name']=='Iris-versicolor']
data2_vi = data2[data2['Name']=='Iris-virginica']

import matplotlib.pyplot as plt

plt.subplot(2,1,1)
plt.scatter(data1_se['SepalLength'], data1_se['SepalWidth'],c='r')
plt.scatter(data1_ve['SepalLength'], data1_ve['SepalWidth'],c='y')
plt.scatter(data1_vi['SepalLength'], data1_vi['SepalWidth'],c='b')

plt.subplot(2,1,2)
plt.scatter(data2_se['PetalLength'], data2_se['PetalWidth'],c='r')
plt.scatter(data2_ve['PetalLength'], data2_ve['PetalWidth'],c='y')
plt.scatter(data2_vi['PetalLength'], data2_vi['PetalWidth'],c='b')
plt.show()