"""
이번에는 DataFrame에서 조건에 해당하는 데이터를 찾는 연습을 해보겠습니다.

'KBS'에서 시청률이 30이 넘은 데이터만 확인해보려면 어떻게 하면 될까요?

2011    35.951
2012    36.163
2013    31.989
2014    31.210
Name: KBS, dtype: float64
주의: 자동 채점 과제입니다. 정답 출력 코드는 print 없이 작성해 주세요. (예시: df)
"""

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.

KBS_df = df['KBS'] > 30

print(df.loc[KBS_df, 'KBS'])
