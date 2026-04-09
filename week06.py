# 배열의 구조와 정보를 파악할 때 사용합니다. (arr가 배열일 때)
# arr.shape: 배열의 크기 (예: (3, 4)는 3행 4열)
# arr.ndim: 차원 수 (1차원, 2차원 등)
# arr.dtype: 요소의 데이터 타입 (int64, float64 등)
# arr.size: 전체 요소의 개수

# 1. 메모리 관련 속성
# arr.itemsize: 각 요소(Element) 하나가 차지하는 바이트(byte) 수입니다.
# arr.nbytes: 배열 전체가 차지하는 총 바이트 수입니다. (itemsize * size와 같습니다.)
# arr.strides: 다음 요소나 다음 행으로 이동하기 위해 메모리상에서 몇 바이트를 건너뛰어야 하는지 나타내는 튜플입니다.
# 2. 데이터 표현 속성
# arr.T: 배열의 전치(Transpose)된 결과입니다. (행과 열을 바꿈)
# arr.flat: 다차원 배열을 1차원으로 펼친 상태의 반복자(Iterator)입니다.
# arr.real / arr.imag: 복소수 배열일 경우 각각 실수부와 허수부를 반환합니다.
# 3. 기타 상태 확인
# arr.flags: 배열의 메모리 배치 방식(C-style인지 Fortran-style인지), 쓰기 가능 여부 등을 보여줍니다.
# arr.base: 이 배열이 다른 배열의 뷰(View)인지, 아니면 독자적인 데이터를 가진 객체인지 확인해 줍니다. (메모리 절약을 위해 슬라이싱할 때 중요합니다.)

import numpy as np

# array01 = np.random.random((2, 3, 3))
array01 = np.random.random((4, 2))
print(array01)
print(array01.shape, array01.dtype, array01.ndim, array01.size)
print(array01.T)

