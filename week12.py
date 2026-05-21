import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
titanic01 = titanic.drop(columns=['embarked', 'alive', 'class', 'deck'])
# print(titanic01.info())
# print(titanic01.isnull().sum())
titanic01 = titanic01.dropna(subset=['embark_town'])
print(titanic01.info())
# print(titanic01['age'].mean())
# print(titanic01['age'].median())
# print(titanic01['age'].mode())
titanic01['age'] = titanic01['age'].fillna(titanic01['age'].median())
print(titanic01.info())

sns.barplot(data=titanic01, x='pclass', y='survived')
plt.show()

