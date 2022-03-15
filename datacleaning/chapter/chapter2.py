# iqr을 통해 데이터 삭제 후 산점도 출력 문제
import pandas as pd

df = pd.read_csv('data/movie_metadata.csv')

# 코드를 작성하세요.
# print(df)

# print(df.describe()['budget'])

q1 = df['budget'].quantile(0.25)
q3 = df['budget'].quantile(0.75)
iqr = q3 - q1

condition = df['budget'] > q3 + 5 * iqr

df.drop(df[condition].index, inplace=True)


df.plot(kind='scatter', x='budget', y='imdb_score')
