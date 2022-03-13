import pandas as pd
import seaborn as sns

df = pd.read_csv('data/survey.csv')

column = df.loc[:, 'Horror':'Action']

corr = column.corr()

sns.clustermap(corr)