import seaborn as sns

ex = sns.load_dataset('exercise')
ex = ex[
    (ex['diet'] == 'low fat') &
    (ex['time'] == '30 min') &
    (ex['kind'] == 'running')
]
print(ex)
mean_pulse = ex['pulse'].mean()
print(mean_pulse)