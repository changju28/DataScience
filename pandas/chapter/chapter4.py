"""
지난 시간에 DataFrame에서 원하는 부분을 선택하는 인덱싱을 배웠는데요. 이를 통해서 값을 찾는 연습을 해봅시다.
2016년도에 KBS방송국의 시청률을 찾아봅시다.
데이터를 한번 잘 살펴보고 어떻게 값을 찾아야 할지 고민해보세요!

주의: 자동 채점 과제입니다. 정답 출력 코드는 print 없이 작성해 주세요. (예시: df)

"""

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)


print(df.loc[2016, 'KBS'])