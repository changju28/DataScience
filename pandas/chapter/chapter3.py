"""
‘메가밀리언’은 ‘파워볼’과 더불어 미국에서 양대산맥을 이루는 복권입니다. 당첨될 확률이 약 3억분의 1 정도로 굉장히 낮은 대신, 당첨시 금액이 어마어마하죠. 2018년에는 한 명이 무려 1.8조원을 가져가기도 했습니다.

메가밀리언 측에서 2002년부터 현재(2/15/19)까지의 당첨 번호가 담긴 mega_millions.csv 파일을 공개했는데요. 이 데이터를 DataFrame에 넣어 봅시다.

날짜(Draw Date)가 이 DataFrame의 인덱스가 되도록 해 주세요!
"""

import pandas as pd

df = pd.read_csv("data/mega_millions.csv", index_col=0)

# 정답 출력
print(df)