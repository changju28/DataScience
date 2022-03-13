import pandas as pd

df = pd.read_csv('data/museum_1.csv')

# 코드를 작성하세요.
df['분류'] = '일반'


df.loc[df['시설명'].str.contains('대학'), '분류'] = '대학'

print(df)

