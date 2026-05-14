import seaborn as sns

ex = sns.load_dataset('exercise')
# print(ex.head(10))
# print(ex.info())
# print(ex['kind'].value_counts())
# print(ex['diet'].value_counts())
# print(len(ex[ex['diet'] == 'low fat']))
# print(ex[ex['diet'] == 'low fat'])
running_df = ex[ex['kind'] == 'running']
#print(running_df)
# sns.catplot(running_df, x='time', y='pulse', hue='diet', kind='point')