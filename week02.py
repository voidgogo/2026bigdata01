scores = [100, 97, 88, 91]
hap, count = 0, 0
for score in scores:
    hap = hap + score
    count = count + 1
average = hap / count
print(average)

