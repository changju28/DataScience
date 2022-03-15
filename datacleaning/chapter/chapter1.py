# 결측값 제거 문제 dropna()

import pandas as pd

df = pd.read_csv('data/steam_1.csv', index_col=0)

# 코드를 작성하세요.

# 정답 출력

print(df.isnull())

print(df.isnull().sum())

df.dropna(inplace=True)

print(df.isnull().sum())

