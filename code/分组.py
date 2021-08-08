import pandas as pd
import numpy as np

df = pd.read_csv('./nba.csv')
# print(df.head())

# df = df.groupby('Team')['Weight'].mean()
# print(df)
pd.set_option('display.max_columns',None)
print(df.head())

# pd['Team'].apply(lambda x:x.replace(' ', '-')).head()
# pd['Team'].apply(lambda x:str(x)+'!', axis=0).head()
print(df.columns)
# df['']
print(df['Team'])

def foo(x):
    return str(x).replace(' ', '-')

# a = df['Team'].apply(lambda x: str(x)+"!")
# a = df['Team'].apply(lambda x: str(x)+"!")
# a = df['Team'].apply(lambda x: str(x).split( ))
# a = df['Team'].apply(foo())
# a = df['Team'].apply(lambda x: str(x).replace(' ', '-'))
a = df['Team'].apply(foo)

print(a.head())
