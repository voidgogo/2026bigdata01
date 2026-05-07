import seaborn as sns

mpg = sns.load_dataset('mpg')
mpg = mpg.drop(columns=['origin', 'model_year', 'name'])
print(mpg.info())
print(mpg.head())
# print(mpg.sort_values('mpg', ascending=False))
mpg['horsepower'] = mpg['horsepower'].fillna(
    mpg.groupby('cylinders')['horsepower'].transform('median')
)
print(mpg.info())
# print(mpg[mpg['horsepower'].isnull()])