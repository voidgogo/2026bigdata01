import pandas as pd

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9], '화':[10, 3, 11]}, index=[1, 2, 3])
print(df)
# df_new = df.iloc[0:3]  # df_new = df.iloc[:]
# df_new = df.iloc[1:3]
# df_new = df.iloc[1:]
df_new = df.iloc[1:,2:]
print(df_new)
