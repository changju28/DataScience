"""
데이터프레임이 있습니다.



코드를 4줄만 써서, 아래 데이터프레임으로 바꿔보세요.



어느 부분이 바뀌었을까요?
눈에 잘 들어오지 않는다면, 하나씩 힌트를 열어 확인해보고 코드를 작성해 보세요.

"""

import pandas as pd

df = pd.read_csv('data/Puzzle_before.csv')

# 코드를 작성하세요.
df['A'] = df['A'] * 2
df[df.loc[:, 'B':'E'] < 80] = 0
df[df.loc[:, 'B':'E'] >= 80] = 1
df.loc[2, 'F'] = 99
print(df)
