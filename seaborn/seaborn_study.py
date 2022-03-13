# import seaborn as sns
# import pandas as pd

# laptops_df = pd.read_csv('data/laptops.csv')
#
#
# sns.catplot(data=laptops_df, x='os', y='price', kind='box')

#lis = [44, 42, 43, 28, 46, 33, 42, 37, 29]
#lis1 = [33, 45, 98, 38, 21, 49, 51, 58, 82, 75]

#lis.sort()
#lis1.sort()
#print(lis1)

import pandas as pd

df = pd.read_csv('data/exam.csv')

df.corr()