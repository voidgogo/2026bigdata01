import pandas as pd

def square(x):
    return x*x

df = pd.DataFrame({'국':[7, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9], '화':[10, 3, 11]}, index=[1, 2, 3])
print(df)
print(df.apply(square))
