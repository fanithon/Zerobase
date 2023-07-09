# # 거듭제곱
#
# num1 = 2
# num2 = 12
# result = num1 ** num2
# print('result: {}'.format(result))

# 제곱근 구하기

# n의 m 제곱근 공식
# n ** (1/m)

# # 2의 제곱근 구하기
# result = 2 ** (1/2)
# print('2의 제곱근 %f' % result)
# print('2의 제곱근 %.2f' % result)
#
# # 2의 3제곱근 구하기
# result = 2 ** (1/3)
# print('2의 3제곱근 %f' % result)
# print('2의 3제곱근 %.2f' % result)
#
# # 2의 4제곱근 구하기
# result = 2 ** (1/4)
# print('2의 4제곱근 %f' % result)
# print('2의 4제곱근 %.2f' % result)

# math 모듈의 sqrt()와 pow() 함수
import math

# sqrt()함수를 이용한 제곱근 구하기

print('2의 제곱근 %f' % math.sqrt(2))
print('2의 제곱근 %.2f' % math.sqrt(2))

print('3의 2제곱근 %f' % math.sqrt(3))
print('3의 2제곱근 %.2f' % math.sqrt(3))

print('4의 2제곱근 %f' % math.sqrt(4))
print('4의 2제곱근 %.2f' % math.sqrt(4))

# pow() 함수를 이용한 거듭제곱 구하기

print('10의 8제곱 %.0f' % math.pow(10, 8))
print('12의 12제곱 %.0f' % math.pow(12, 12))

# 실습
'''
아들이 엄마한테 용돈을 받는데, 첫달에는 200원을 받고 매월 이전 달의 2배씩 인상하기로 함.
12개월 째 되는 달에는 얼마를 받을 수 있는지 계산해보자.
'''
firstMoney = 200
after12Month = ((firstMoney * 0.01) ** 12 ) * 100

print('12개월 째 되는 달 받는 용돈 :{}'.format(after12Month))
after12Month = int(after12Month)
strResult = format(after12Month, ',')
print(strResult, '원')
print(type(strResult))