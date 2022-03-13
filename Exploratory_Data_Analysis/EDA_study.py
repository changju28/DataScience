import pandas as pd
import seaborn as sns

# df = pd.read_csv('data/young_survey.csv')

# basic_info = df.iloc[:, 140:]
# basic_info.head()

# print(basic_info.describe())

# print(basic_info['Gender'].value_counts())
# print()
# print(basic_info['Handedness'].value_counts())
# print()
# print(basic_info['Education'].value_counts())

#sns.violinplot(data=basic_info, y='Age')

#sns.violinplot(data=basic_info, x='Gender', y='Age')

#sns.violinplot(data=basic_info, x='Gender', y='Age', hue='Handedness')

# sns.jointplot(data=basic_info, x='Height', y='Weight')

# df = pd.read_csv('data/occupations.csv')

# F = df.loc[df['gender'] == 'F', 'occupation']
# M = df.loc[df['gender'] == 'M']

# print(F.value_counts())
# print()
# print(M['occupation'].value_counts())

# df = pd.read_csv('data/young_survey.csv')

# music = df.iloc[:, :19]

#print(music.head())

# sns.heatmap(music.corr())

# print(df.corr()['Age'].sort_values(ascending=False))

# print(df.loc[:, 'Getting up'])


# print(df.loc[early, df.iloc[:, :19]])

# branch_df = df.corr()['Getting up']

# print(branch_df[1:19].sort_values(ascending=True))

# a = df.corr()['Musical instruments']
# b = df.corr()['Spending on looks']
# c = df.corr()['Writing notes']
# d = df.corr()['Workaholism']

# print(a['Writing'])
# print(b['Branded clothing'])
# print(c['New environment'])
# print(d['Healthy eating'])

# interests = df.loc[:, 'History':'Pets']
# print(interests)
#
# corr = interests.corr()
# print(corr)
#
# print(corr['History'].sort_values(ascending=False))
#
# sns.clustermap(corr)

df = pd.read_csv('data/titanic.csv')

# age = df['Age'].value_counts().sort_values()
# print(age)
# fare = df[['Fare', 'Age']].value_counts().sort_values(ascending=True)
# print(fare)
#
# survived = df['Survived'].value_counts()
#
# print(survived)
#
# pclass = df[['Pclass', 'Survived']].value_counts()
#
# print(pclass)
#
# a = df.loc[df['Survived'] == 1, 'Age'].value_counts()
# b = df.loc[:, ['Sex', 'Survived']].value_counts()
#
# print(a)
# print(b)

print(df.info())

# df.plot(kind='hist', y='Age', bins=30)

df.plot(kind='scatter', x='Age', y='Fare')