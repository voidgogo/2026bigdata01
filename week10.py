import seaborn as sns

mpg = sns.load_dataset('mpg')
# print(mpg.head())
# print(mpg.info())
# print(mpg.describe())
# print(mpg['cylinders'].value_counts())
print(mpg[mpg['horsepower'].isnull()])
mpg['horsepower'] = mpg['horsepower'].fillna(
    mpg.groupby('cylinders')['horsepower'].transform('median')
)
print(mpg.info())
print(mpg[mpg['horsepower'].isnull()])