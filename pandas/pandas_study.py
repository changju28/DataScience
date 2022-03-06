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

iphone_df = pd.read_csv("iphone.csv", index_col=0)

# print(iphone_df)

# print(iphone_df.loc['iPhone 8', '메모리'])
# print(iphone_df.loc['iPhone X'])
# print(type(iphone_df.loc['iPhone X']))
# print(iphone_df.loc[:, '출시일'])
# print(iphone_df['출시일'])

print(iphone_df.loc['iPhone 8': 'iPhone XS'])
print()
print(iphone_df.loc[:, '메모리':'Face ID'])