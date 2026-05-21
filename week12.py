import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic[['alive', 'survived', 'pclass', 'class', 'embarked', 'embark_town']])
titanic01 = titanic.drop(columns=['embarked', 'alive', 'class', 'deck'])
# print(titanic01.info())
# print(titanic01['deck'])
# print(titanic01['pclass'].value_counts())
# print(titanic01[titanic01['pclass'] == 3])
# survival_rate = titanic01['survived'].mean()
survival_rate_pclass = titanic01.groupby('pclass')['survived'].mean()
# print(survival_rate_pclass)
survival_rate_sex = titanic01.groupby('sex')['survived'].mean()
print(survival_rate_sex)
