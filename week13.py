import seaborn as sns
# import matplotlib.pyplot as plt

health = sns.load_dataset("healthexp")
# print(health.head())
# print(health.tail(7))
# print(health.info())
# print(health.describe())
print(health['Country'].unique())
print(health['Country'].nunique())
print(health['Country'].value_counts())