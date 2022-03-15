import pandas as pd

## 데이터 클리닝 결측값 제거 및 생성
# df = pd.read_csv('data/attendance.csv', index_col=0)

# print(df)

# 결측값 존재 유무 확인 isnull()
"""
print(df.isnull())
"""

# 결측값 존재 컬럼의 합 isnull().sum()
"""
print(df.isnull().sum())
"""

# 결측값 제거 dropna()
"""
df.dropna(inplace=True)

print(df)
"""

# 결측값 존재 컬럼 삭제 dropna(axis='columns')
"""
df.dropna(axis='columns', inplace=True)

print(df)
"""

# 결측값 대체 fillna(값)
"""
#_1 결측값 숫자 넣기
df.fillna(0, inplace=True)

#_2 결측값 평균 넣기
df.fillna(df.mean(), inplace=True)

#_3 결측값 중간값 넣기
df.fillna(df.median(), inplace=True)
print(df)
"""

## 중복된 row / columns 삭제
# df = pd.read_csv('data/dust.csv', index_col=0)

# 중복 데이터 확인
"""
print(df.index.value_counts())

print(df.loc['07월 31일'])
"""

# 중복된 row 삭제 drop_duplicates
"""
df.drop_duplicates(inplace=True)

print(df.index.value_counts())
"""

# 중복된 columns 삭제
"""
#_1 row 와 columns 교체 T
print(df.T)

#_2 바뀐 row에 중복값 삭제 drop_duplicates
print(df.T.drop_duplicates())

#_3 다시 row와 columns 변경 후 dataframe 변수에 저장
df = df.T.drop_duplicates().T

print(df)
"""

## 이상점 을 찾고 수정 및 삭제
# df = pd.read_csv('data/beer.csv', index_col=0)

# print(df)

"""
#_1 box plot 을 통해 이상점 찾기
# df.plot(kind='box', y='abv')

#_2 box plot의 25% 지점과 75% 지점위치 찾기 describe()
print(df['abv'].describe())

#_2_1 25% 지점 받아오기
print(df['abv'].quantile(0.25))

#_2_2 75% 지점 받아오기
print(df['abv'].quantile(0.75))

#_3 각 지점 변수로 저장 후 iqr 값 저장
q1 = df['abv'].quantile(0.25)
q3 = df['abv'].quantile(0.75)
iqr = q3 - q1

#_3 이상점 찾기 공식 25% 보다 작고 1.5 * iqr 보다 작거나 | 75% 보다 크고 1.5 * iqr 보다 크거나
condition = (df['abv'] < q1 - 1.5 * iqr) | (df['abv'] > q3 + 1.5 * iqr)

#_4 이상점 출력
print(df[condition].T)

#_5 이상점 수정
df.loc[2250, 'abv'] = 0.055

print(df.loc[2250])

condition = (df['abv'] < q1 - 1.5 * iqr) | (df['abv'] > q3 + 1.5 * iqr)
print([df[condition]])

#_6 이상점 삭제 이상점의 인덱스를 가져온뒤 drop으로 날려줌
print(df[condition].index)

df.drop(df[condition].index, inplace=True)

print(df)

df.plot(kind='box', y='abv')
"""

## 이상점 을 산점도로 찾고 삭제
# df = pd.read_csv('data/exam_outlier.csv')

"""
# print(df)
#_1 산점도 출력 후 이상점 찾기
# df.plot(kind='scatter', x='reading score', y='writing score')

#_1_1 상관계수 출력
print(df.corr())

#_2 산점도로 찾은 이상점의 index 번호를 찾는다
print(df[df['writing score'] > 100])
#_2_1 찾은 index 번호를 삭제
df.drop(51, inplace=True)

#_3 삭제 후 산점도 출력
# df.plot(kind='scatter', x='reading score', y='writing score')
#_3_1 삭제 후 상관계수 출력
print(df.corr())

#_4 산점도로 찾은 이상점 index 번호를 찾는다
print(df[(df['writing score'] > 80) & (df['reading score'] < 40)])
#_4_1 찾은 index 번호를 삭제
df.drop(373, inplace=True)

#_5 데이터 분석을 위한 산점도 와 상관계수가 알맞을 때까지 반복
df.plot(kind='scatter', x='reading score', y='writing score')

print(df.corr())
"""

