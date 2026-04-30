import pandas as pd

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9]}, index=[1, 2, 3])
print(df)
# df_new = pd.melt(df)
# df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'})
df_new = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5')
print(df_new)