import numpy as np

## 리스트 생성

# array1 = np.full(6, 0)
# array2 = np.zeros(6, dtype=int)
# array3 = np.full(6, 1)
# array4 = np.ones(9, dtype=int)
# array5 = np.random.random(6)
# array6 = np.random.random(10)
# array7 = np.arange(6)
# array8 = np.arange(2, 7)
# array9 = np.arange(3, 17, 3)
#
#
# print("full: {}".format(array1))
# print("zeros: {}".format(array2))
# print("full: {}".format(array3))
# print("ones: {}".format(array4))
# print("random.random: {}".format(array5))
# print("random.random: {}".format(array6))
# print("arange(숫자): {}".format(array7))
# print("arange(숫자, 숫자): {}".format(array8))
# print("arange(숫자, 숫자, 숫자): {}".format(array9))

## 슬라이싱

# array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
#
# print(array1[0])
# print(array1[2:7])
# array2 = np.array([2, 1, 3])
# print(array1[array2])

## numpy 리스트 덧셈/뺄셈/나눗셈/곱셈... 출력

# array1 = np.arange(10)
# array2 = np.arange(10, 20)
#
# print(array1)
# print(array2)
#
# print(array1 * 2)
# print(array1 / 2)
#
# print(array1 + array2)
# print(array1 * array2)


## numpy boolean 연산
# array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
#
# print(array1 > 4)
#
# print(array1 % 2 == 0)
#
# booleans = np.array([True, False, False, False, False, False, True, False, True, False])
#
# print(np.where(booleans))
#
# filter_array1 = np.where(array1 > 4)
#
# print(array1[filter_array1])

## numpy 기본 통계
#1 최댓값 최솟값
# array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
#
# print(array1.max())
# print(array1.min())
#
# #2 평균값
# array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])
#
# print(array1.mean()) # 평균값
#
# #3 중앙값
#
# array1 = np.array([8, 12, 9, 15, 16])
# array2 = np.array([14, 6, 13, 21, 23, 31, 9, 5])
#
# print(np.median(array1))
# print(np.median(array2))
#
# #4 표준편차 분산
#
# array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])
#
# print(array1.std())
# print(array1.var())

