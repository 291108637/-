import pandas as pd
import numpy as np

"""
1.读取.csv .txt .xls .xlsx 
2.写入.csv .xls .xlsx
3.基本数据结构Series DataFrame 
4.常用基本函数
5.排序
"""

df = pd.read_csv('./nba.csv')
df_txt = pd.read_table('data/table.txt')  # 可设置sep分隔符参数
df_excel = pd.read_excel('data/table.xlsx')  # 需要安装xlrd包

df.to_csv('data/new_table.csv')
df.to_csv('data/new_table.csv', index=False)  # 保存时除去行索引
df.to_excel('data/new_table2.xlsx', sheet_name='Sheet1')  # 需要安装openpyxl

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'], name='这是一个Series', dtype='float64')
print(s.values, s.name, s.index, s.dtype)
print(s['a'], s.mean())
print([attr for attr in dir(s) if not attr.startswith('_')])

df = pd.DataFrame({'col1': list('abcde'), 'col2': range(5, 10), 'col3': [1.3, 2.5, 3.6, 4.6, 5.8]}, index=list('一二三四五'))
print(df['col1'], type(df), type(df['col1']), )
df.rename(index={'一':'one'},columns={'col1':'new_col1'})
print(df.index, df.columns, df.values, df.shape, df.mean())
df.mean()    # 本质上是一种Aggregation操作，将在第3章详细介绍


df.drop(index='五',columns='col1')    # 设置inplace=True后会直接在原DataFrame中改动

df['col1']=[1,2,3,4,5]
del df['col1']
df['col1']=[1,2,3,4,5]
df.pop('col1')
df['B']=list('abc')
df.assign(C=pd.Series(list('def')))     # assign方法不会对原dataframe做修改

df.select_dtypes(include=['number']).head()
df.select_dtypes(include=['float']).head()

df['Math'].apply(lambda x:str(x)+'!').head()    # 可以使用lambda表达式，也可以使用函数
df.apply(lambda x:x.apply(lambda x:str(x)+'!')).head()  # 这是一个稍显复杂的例子，有利于理解apply的功能

df.head()  # 读取前5行
df.tail()  # 读取后5行




