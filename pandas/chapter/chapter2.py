"""
아기의 성별과 어머니의 인종에 따른, 뉴욕에서 가장 인기 있는 아기 이름이 무엇인지 조사를 해 봤습니다.

조사 결과가 data 폴더의 popular_baby_names.csv라는 파일에 담겨 있는데요. 안에 있는 정보를 DataFrame으로 읽어 들이고, DataFrame을 출력해 주세요.

주의: 자동 채점 과제입니다. 정답 출력 코드는 print 없이 작성해 주세요. (예시: df)
"""

import pandas as pd

df = pd.read_csv("data/popular_baby_names.csv")

# 정답 출력
print(df)