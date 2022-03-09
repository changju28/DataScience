import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# print(df)
# adobe = df['company'] == 'Adobe'
# cnt = df['count'] > 0
# not_total = df['job_category'] != 'Totals'
# not_Previous_totals = df['job_category'] != 'Previous_totals'
#
# job = df.loc[adobe & cnt & not_total & not_Previous_totals, ['job_category', 'count']]
# job.set_index('job_category', inplace=True)
#
# adobe_dict = {}
# unique_job = list(job.index.unique())
# for i in unique_job:
#     total = int(job.loc[job.index == i].sum())
#     adobe_dict[i] = total
#
# # print(adobe_dict)
# # plt.pie(adobe_dict.values(), labels=adobe_dict.keys())
# # plt.show()
# df = pd.DataFrame([adobe_dict])
# df.rename(index={0: 'count'}, inplace=True)
# print(df)
# 코드를 작성하세요.

# 방법 1
# adobe = (df['company'] == 'Adobe') & (df['race'] == 'Overall_totals') & (df['count'] != 0)
# except_total = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')
# abobe_job = df[adobe & except_total]
# abobe_job.set_index('job_category', inplace=True)
# abobe_job.plot(kind='pie', y= 'count')

boolean_adobe = df['company'] == 'Adobe'
boolean_all_races = df['race'] == 'Overall_totals'
boolean_count = df['count'] != 0
boolean_job_category = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')

df_adobe = df[boolean_adobe & boolean_all_races & boolean_count & boolean_job_category]
df_adobe.set_index('job_category', inplace=True)
df_adobe.plot(kind='pie', y= 'count')