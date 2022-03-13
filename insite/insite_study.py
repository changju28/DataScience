import pandas as pd
import seaborn as sns

"""
# sum 활용
df = pd.read_csv('data/broadcast.csv', index_col=0)

#df.plot()

#print(df.sum(axis='columns'))

df['Total'] = df.sum(axis='columns')

#df.plot(y='Total')

df['Group1'] = df.loc[:, 'KBS':'SBS'].sum(axis='columns')
df['Group2'] = df.loc[:, 'TV CHOSUN':'MBN'].sum(axis='columns')

#print(df)

df.plot(y=['Group1', 'Group2'])
"""

"""
# 포함된 값 찾기 str.contains(문자내 포함) / str.startswith(첫글자 포함)
df = pd.read_csv('data/albums.csv')

# print(df)

# print(df['Genre'].unique())

# print(df[df['Genre'].str.contains('Blues')])
print(df[df['Genre'].str.startswith('Blues')])
"""

"""
# 문자열 분리
df = pd.read_csv('data/parks.csv')

address = df['소재지도로명주소'].str.split(n=1, expand=True)

df['관활구역'] = address[0]

print(df)
"""
"""
# 카테고리 분류
df = pd.read_csv('data/laptops.csv')

# print(df)

brand_nation = {
    'Dell': 'U.S.',
    'Apple': 'U.S.',
    'Acer': 'Taiwan',
    'HP': 'U.S.',
    'Lenovo': 'China',
    'Alienware': 'U.S.',
    'Microsoft': 'U.S.',
    'Asus': 'Taiwan'
}
# df['brand'].map(brand_nation)
# print(df['brand'].map(brand_nation))

df['brand nation'] = df['brand'].map(brand_nation)

# print(df)
"""
"""
# groupby
nation_group = df.groupby('brand nation')
print(type(nation_group))

print(nation_group.count())

print(nation_group.max())

print(nation_group.mean())

print(nation_group.first())
print(nation_group.last())
"""

"""
# 데이터 합치기
df1 = pd.read_csv('data/vegetable_quantity.csv')
df2 = pd.read_csv('data/vegetable_price.csv')

# print(df1)
# print(df2)

print(pd.merge(df1, df2, on='Product'))
print()
print(pd.merge(df1, df2, on='Product', how='left'))
print()
print(pd.merge(df1, df2, on='Product', how='right'))
print()
print(pd.merge(df1, df2, on='Product', how='outer'))
"""

