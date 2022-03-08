import pandas as pd
import numpy as np

# two_dimensional_list = [["dongwook", 50, 86], ["seneui", 89, 31], ["ikjoong", 68, 91], ["yoonsoo", 88, 75]]
#
# my_df = pd.DataFrame(two_dimensional_list, columns=["name", "english_score", "math_score"], index=["a", "b", "c", "d"])
#
# print(my_df)
#
# print(type(my_df))
#
# print(my_df.index)
# print(my_df.columns)
#
# print()
#
# print(my_df.dtypes)

## pandas list DataFrame

# two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
# two_dimensional_array = np.array(two_dimensional_list)
# list_of_series = [
#     pd.Series(['dongwook', 50, 86]),
#     pd.Series(['sineui', 89, 31]),
#     pd.Series(['ikjoong', 68, 91]),
#     pd.Series(['yoonsoo', 88, 75])
# ]
#
# # 아래 셋은 모두 동일합니다
# df1 = pd.DataFrame(two_dimensional_list)
# df2 = pd.DataFrame(two_dimensional_array)
# df3 = pd.DataFrame(list_of_series)
#
# print(df1)
# print()
# print(df2)
# print()
# print(df3)

## pandas dictionary DataFrame

# names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
# english_scores = [50, 89, 68, 88]
# math_scores = [86, 31, 91, 75]
#
# dict1 = {
#     'name': names,
#     'english_score': english_scores,
#     'math_score': math_scores
# }
#
# dict2 = {
#     'name': np.array(names),
#     'english_score': np.array(english_scores),
#     'math_score': np.array(math_scores)
# }
#
# dict3 = {
#     'name': pd.Series(names),
#     'english_score': pd.Series(english_scores),
#     'math_score': pd.Series(math_scores)
# }
#
#
# # 아래 셋은 모두 동일합니다
# df1 = pd.DataFrame(dict1)
# df2 = pd.DataFrame(dict2)
# df3 = pd.DataFrame(dict3)
#
# print(df1)

# pandas 리스트가 담긴 사전이 아니라 사전이 담긴 리스트로 DataFrame을 만들 수 있다

# my_list = [
#     {'name': 'dongwook', 'english_score': 50, 'math_score': 86},
#     {'name': 'sineui', 'english_score': 89, 'math_score': 31},
#     {'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
#     {'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
# ]
#
# df = pd.DataFrame(my_list)
# print(df)

# iphone_df = pd.read_csv("iphone.csv", index_col=0)

# print(iphone_df)

# print(iphone_df.loc['iPhone 8', '메모리'])
# print(iphone_df.loc['iPhone X'])
# print(type(iphone_df.loc['iPhone X']))
# print(iphone_df.loc[:, '출시일'])
# print(iphone_df['출시일'])

# print(iphone_df.loc['iPhone 8': 'iPhone XS'])
# print()
# print(iphone_df.loc[:, '메모리':'Face ID'])

# print(iphone_df.loc[[True, False, True, True, False, True, False]])
# print(iphone_df.loc[[True, False, True, True]])

# print(iphone_df.loc[:, [True, False, False, True]])

# print(iphone_df['디스플레이'] > 5)
# print(iphone_df.loc[iphone_df['디스플레이'] > 5])

# print(iphone_df.loc[iphone_df['Face ID'] == 'Yes'])
# print((iphone_df['Face ID'] == 'Yes') & (iphone_df['디스플레이'] > 5))

# print(iphone_df.iloc[[2, 4]])

# print(iphone_df.iloc[[1, 3], [1, 4]])
# print(iphone_df.iloc[3:, [1, 4]])

# liverpool_df = pd.read_csv('liverpool.csv', index_col=0)
# print(liverpool_df)
# print()
# liverpool_df.rename(columns={'position': 'Position'}, inplace=True)
# # print(liverpool_df)
# liverpool_df.index.name = 'Player Name'
# # print(liverpool_df)
#
# liverpool_df['Player Name'] = liverpool_df.index
# liverpool_df.set_index('number', inplace=True)
# print(liverpool_df)

# laptops_df = pd.read_csv('laptops.csv')

# print(laptops_df.head(3))
# print(laptops_df.tail(6))

# print(laptops_df.shape)

# print(laptops_df.columns)

# print(laptops_df.info)
# print(laptops_df.describe())

# print(laptops_df.sort_values(by='price', ascending=False))

# print(laptops_df['brand'].unique())
# print(laptops_df['brand'].value_counts())
# print(laptops_df['brand'].describe())

df = pd.read_csv('world_cities.csv')

# print(world_cities['City / Urban area'].describe())
# print()
# print(world_cities['Country'].describe())

# print((world_cities['Population'] / world_cities['Land area (in sqKm)']) > 10000)

# print(world_cities[(world_cities['Population'] / world_cities['Land area (in sqKm)']) > 10000].count())
# world_cities['a'] = (world_cities['Population'] / world_cities['Land area (in sqKm)']) > 10000
# print(world_cities['Country'])
# print(world_cities['Country'].describe())
# print(world_cities.loc[world_cities['a']==True])

# df["Density"] = df["Population"] / df["Land area (in sqKm)"]

# df_high_density = df[df["Density"] > 10000]

# print(df_high_density.sort_values('Density', ascending=False))

cont = df['Country'].value_counts()
print(cont[cont == 4].keys())