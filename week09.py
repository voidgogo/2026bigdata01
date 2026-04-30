import pandas as pd

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9], '화':[10, 3, 11]}, index=[1, 2, 3])
print(df)
print(df.iat[1, 2])
print(df.at[2, '수'])
print(df.sample(frac=0.33))
print(df.nsmallest(2, '화'))
print(df.tail(2))