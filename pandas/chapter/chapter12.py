"""
키와 몸무게가 담겨 있는 한 DataFrame이 있는데요. 몇 가지 잘못된 사항들이 있습니다. 이번 챕터에서 배운 기법들로 DataFrame을 바로잡아 봅시다.

해야 할 일이 두 가지 있습니다.

'비만도' column을 추가하고, 모든 ID에 대해 '정상'으로 설정해주세요.
'Gender' column의 값을 ID 0~10까지는 'Male' 11~20까지는 'Female'로 변경하세요.

"""

import pandas as pd

df = pd.read_csv('data/body_imperial2.csv', index_col=0)

df.loc[:10, 'Gender'] = 'Male'
df.loc[11:, 'Gender'] = 'Famale'
# 코드를 작성하세요.
df['비만도'] = '정상'
# 정답 출력
print(df)