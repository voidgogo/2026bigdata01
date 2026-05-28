import seaborn as sns

# 피실험자, 측정시간, 자극종류, 뇌부위, 뇌측정신호
fmri = sns.load_dataset("fmri")
# print(fmri.head())
# print(fmri.tail())
# print(fmri.describe())
# print(fmri.info())
# print(fmri.groupby(['region', 'event'])['signal'].mean())
# print(fmri.groupby(['region', 'event'])['signal'].std())
# print(fmri.groupby(['region', 'event'])['signal'].max())
# print(fmri.groupby(['region', 'event'])['signal'].min())
print(fmri.groupby(['region', 'event'])['signal'].agg(['mean', 'std', 'max', 'min']))
