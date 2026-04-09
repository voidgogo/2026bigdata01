# 리스트로 생성: np.array([1, 2, 3])
# 연속 값 생성: np.arange(0, 10, 2) (0부터 10 미만까지 2씩 증가)
# 특수 배열:
# np.zeros((2, 3)) : 0으로 채워진 2행 3열 배열
# np.ones((2, 3)) : 1로 채워진 2행 3열 배열
# np.full((2, 2), 7) : 모든 요소를 7로 채움
# 난수 생성: np.random.rand(2, 3) (0~1 사이의 랜덤 값)

import numpy as np

l1 = [1, 2, 3]
array01 = np.array(l1)
print(l1)
print(array01)

array02 = np.arange(0, 10, 2)
print(array02)

array03 = np.zeros((2, 3))
print(array03)

array04 = np.ones((2, 3))
print(array04)

array05 = np.full((2, 3), -1)
print(array05)

array06 = np.random.rand(2, 3)
print(array06)

array07 = np.linspace(0, 10, 3)
print(array07)
