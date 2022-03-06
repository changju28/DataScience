"""
이번에는 DataFrame에서 여러 줄을 찾는 연습을 해보겠습니다. SBS와 JTBC의 시청률만 확인하려면 어떻게 하면 될까요?
"""

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.

print(df.loc[:, ['SBS', 'JTBC']])
print()
print(df[['SBS', 'JTBC']])