"""
키와 몸무게가 담겨 있는 한 DataFrame이 있는데요. 몇 가지 잘못된 사항들이 있습니다. 이번 챕터에서 배운 기법들로 DataFrame을 바로잡아 봅시다.

해야 할 일이 세 가지 있습니다.

ID 1의 무게를 200으로 변경하세요.
ID 21의 row를 삭제하세요.
ID 20의 row를 추가하세요. ID 20의 키는 70, 무게는 200입니다.
딱 3줄의 코드만 추가하시면 됩니다!

주의: 자동 채점 과제입니다. 정답 출력 코드는 print 없이 작성해 주세요. (예시: df)
"""

import pandas as pd

df = pd.read_csv('data/body_imperial1.csv', index_col=0)

# 코드를 작성하세요.

df.loc[1, 'Weight (Pound)'] = 200
df.drop(21, axis='index', inplace=True)
df.loc[20, ['Height (Inch)', 'Weight (Pound)']] = [70, 200]
print(df)
# 정답 출력
# df