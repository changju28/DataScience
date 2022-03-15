# 예산이 높은 상위 15개 영화 제거
import pandas as pd

df = pd.read_csv('data/movie_metadata.csv')

# 코드를 작성하세요.
condition = df['budget'].sort_values(ascending=False).index[:15]

df.drop(condition, inplace=True)

df.plot(kind='scatter', x='budget', y='imdb_score')
