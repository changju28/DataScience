"""
이번에는 좀 더 DataFrame을 다방면으로 분석해봅시다.

주어진 데이터에서 SBS가 TV CHOSUN보다 더 시청률이 낮았던 시기의 데이터를 확인해보려고 합니다.

어떻게 하면 될까요?

"""

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.

boolean_df = df['SBS'] < df['TV CHOSUN']

print(df.loc[boolean_df, ['SBS', 'TV CHOSUN']])