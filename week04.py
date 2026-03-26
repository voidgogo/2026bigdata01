import pandas as pd
scores = [100, 97, 88, 91]
average = pd.Series(scores).min()
print(average)
