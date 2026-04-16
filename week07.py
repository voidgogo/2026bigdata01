# 3) 넘파이 배열 연산
import numpy as np
import random

# l1 = [9, '짬뽕', 3.7, [1, 2, 3]]  # 정수, 문자열, 실수, 리스트
# l1 = [9, '짬뽕', 3.7]  # 정수, 문자열, 실수
# array01 = np.array(l1)
# print(l1)
# print(array01)
#
array02 = np.arange(1, 10)
print(array02)
#
# array03 = np.ones((2, 4), dtype=int)
# print(array03)
# print(array03.T)

l2 = list()
# array04 = np.random.rand(2, 3)
# print(array04)
# print(array04.transpose())
l3 = []
for i in range(3):
    l2.append(random.random())
print(l2)

for item in l2:
    l3.append(item * 10)
print(l3)

array04 = np.array(l2)
print(array04 * 10)
print(array04 > 0.5)

# 4) 넘파이 배열 주요 통계함수
print(np.mean(array02))
print(np.median(array02))
print(np.max(array02))
print(np.min(array02))
print(np.var(array02))
print(np.std(array02))