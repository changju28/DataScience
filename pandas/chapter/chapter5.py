"""
이번에는 DataFrame에서 한 줄을 찾는 연습을 해보겠습니다.
JTBC의 시청률을 확인하려면 어떻게 해야 할까요?

2011    7.380
2012    7.878
2013    7.810
2014    7.490
2015    7.267
2016    7.727
2017    9.453
Name: JTBC, dtype: float64
주의: 자동 채점 과제입니다. 정답 출력 코드는 print 없이 작성해 주세요. (예시: df)

"""

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.

print(df.loc[:, 'JTBC'])