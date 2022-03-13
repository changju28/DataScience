import pandas as pd

df = pd.read_csv('data/museum_2.csv')

# 코드를 작성하세요.

first_number = df['운영기관전화번호'].str.split('-', expand=True)

df['지역번호'] = first_number[0]
print(df)