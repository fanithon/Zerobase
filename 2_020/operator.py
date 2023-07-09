# 모듈이란, 누군가 이미 만들어 놓은 훌륭한 기능 (공짜로 사용 가능)

import operator

num1 = 8
num2 = 4

print('{} + {} = {}'.format(num1, num2, operator.add(num1,num2)))        # 더하기
print('{} - {} = {}'.format(num1, num2, operator.sub(num1,num2)))        # 뺴기
print('{} * {} = {}'.format(num1, num2, operator.mul(num1,num2)))        # 곱하기
print('{} / {} = {}'.format(num1, num2, operator.truediv(num1,num2)))    # 나누기
print('{} % {} = {}'.format(num1, num2, operator.mod(num1,num2)))        # 나머지
print('{} // {} = {}'.format(num1, num2, operator.floordiv(num1,num2)))  # 몫
print('{} ** {} = {}'.format(num1, num2, operator.pow(num1,num2)))       # 거듭제곱

# 비교 연산자 관련 함수
print('{} == {} : {}'.format(num1, num2, operator.eq(num1, num2)))
print('{} != {} : {}'.format(num1, num2, operator.ne(num1, num2)))
print('{} > {} : {}'.format(num1, num2, operator.gt(num1, num2)))
print('{} >= {} : {}'.format(num1, num2, operator.ge(num1, num2)))
print('{} < {} : {}'.format(num1, num2, operator.lt(num1, num2)))
print('{} <= {} : {}'.format(num1, num2, operator.le(num1, num2)))

# 논리 연산자 관련 함수
flag1 = True
flag2 = False
print('{} and {} : {}'.format(flag1, flag2, operator.and_(flag1,flag2)))
print('{} or {} : {}'.format(flag1, flag2, operator.or_(flag1,flag2)))
print('{} not {} : {}'.format(flag1, flag2, operator.not_(flag1)))

# 백신 접종 대상자 출력 코드를 operator 모듈을 이용해서 변경해보자.

age = int(input('나이 입력:'))
vaccine = operator.or_(operator.lt(age, 20),operator.ge(age,65))
print('age : {}, result: {}'.format(age, vaccine))

# random과 operator 모듈을 사용해서 10부터 100사이의 난수 중 십의 자리와 일의 자리가
# 각각 3의 배수인지 판단하는 코드를 작성해 보자.

import random

rInt = random.randint(10, 100)

num10 = operator.floordiv(rInt, 10)
num1 = operator.mod(rInt, 10)

print('난수 : {}'.format(rInt))
print('십의 자리 : {}'.format(num10))
print('일의 자리 : {}'.format(num1))

print('십의 자리는 3의 배수이다. : {}'.format(operator.mod(num10, 3) == 0))
print('일의 자리는 3의 배수이다. : {}'.format(operator.mod(num1, 3) == 0))