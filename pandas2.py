#对于上述变量df，完成以下要求： 
#1. 创建变量r1 = 将df中所有大于3的值乘方，其他值不变 
#2. 创建变量r2 = df中含有1或4的行 
#3. 创建变量r3 = df中随机一列 
#4. 创建变量r4 = 在df的基础上添加一列add：值为列one与列two的值相加应该如何实现 
#5. 创建变量r5 = df中one列>2的行

import pandas as pd
d = {
    'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 
    'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)


#1 
r1=df.copy()
for i in range(0,df.shape[1]):
     for j in range(0,df.shape[0]):
          if df.iloc[j,i] > 3 :
             r1.iloc[j,i] =  df.iloc[j,i]**2     
print('r1:',r1) 
#r1[r1>3] **=2
  
#2 
r2 = df[(df['one'] == 1) | (df['two'] == 4)]
print('r2:',r2) 
   
#3
import random
r3 = df.copy()
a = random.randint(0,1)
r3 = r3.iloc[:,a]
print('r3:',r3) 
 
 #4
r4 = df.copy()
r4['add'] = r4['one'] + r4['two']
print('r4:',r4) 
 
 #5
r5 = df[ df['one']>2] 
print('r5:',r5) 

