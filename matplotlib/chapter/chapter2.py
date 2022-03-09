"""
실리콘 밸리에서 일하는 사람들의 정보가 있습니다.

직업 종류, 인종, 성별 등이 포함되어 있는데요.

실리콘 밸리에서 일하는 남자 관리자 (Managers)에 대한 인종 분포를 막대 그래프로 다음과 같이 그려보세요.

"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/silicon_valley_summary.csv', index_col=0)
jab = df.index == 'Managers'
gender = df['gender'] == 'Male'
Managers_Male = df.loc[jab & gender, ['race_ethnicity', 'count']]
Managers_Male.set_index('race_ethnicity', inplace=True)
plt.plot(Managers_Male.iloc[:4])
plt.savefig("exam1.png")
plt.show()
# a = df.loc[df['gender'] == 'Male', ['race_ethnicity', 'count']]
# a.set_index('race_ethnicity', inplace=True)
# print(a)
# print(gender)
# 코드를 작성하세요.