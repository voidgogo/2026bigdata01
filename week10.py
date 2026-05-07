import pandas as pd

# df1 = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8]}, index=[1, 2, 3])
# df2 = pd.DataFrame({'국':[9, 6, 17], '수':[3, 5, 9]}, index=[1, 2, 4])
# print(pd.merge(df1, df2, how='left', on='국'))

df = pd.DataFrame({'국':[7, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9], '화':[10, 3, 11]}, index=[1, 2, 3])
print(df)
# print(df.describe())
# print(df.info())
# print(df['국'].value_counts())
# print(len(df))
# print(df.shape)
# print(df['국'].nunique())
print(df.dtypes)