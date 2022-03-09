"""
주어진 데이터를 이용해서 한국, 미국, 영국, 독일, 중국, 일본의 GDP 그래프를 그려 보세요.
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/gdp.csv', index_col=0)

plt.plot(df[['Korea_Rep', 'United_States', 'United_Kingdom', 'Germany', 'China', 'Japan']])
plt.savefig("exam.png")
plt.show()
# 코드를 작성하세요.