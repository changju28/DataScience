import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 코드를 작성하세요.

group_age = df.groupby('occupation')

print(group_age.mean().sort_values(by='age'))

# print(df)