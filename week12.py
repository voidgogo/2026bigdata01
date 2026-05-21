import seaborn as sns

titanic = sns.load_dataset('titanic')
#print(titanic.head())
#print(titanic.describe())
print(titanic.info())
# print(titanic['who'])
# print(titanic['who'].value_counts())
# print(titanic[['embarked', 'embark_town']])
