# 정수를 이용한 덧셈

num1 = 9
num2 = 3

print(f'num1 + num2 : {num1+num2}')

# 실수를 이용한 덧셈

fNum1 = 3.14
fNum2 = 0.12
fResult = fNum1 + fNum2

print(f'fResult : {fResult}')
print('fResult : %.2f' % fResult)

# 정수와 실수를 이용한 덧셈

result = num1 + fNum2
print(f'num1 + num2 : {result}')

# 문자를 이용한 덧셈
str1 = "Squat, "
str2 = "BenchPress, "
str3 = "Deadlift"
strResult = str1 + str2 + str3
print(f'strResult : {strResult}')

# *실습* 국어/영어/수학 점수를 입력하고 합계를 출력해보자.
korean = int(input('국어점수:'))
english = int(input('영어점수:'))
math = int(input('수학점수:'))

totalScore = korean + english + math

print(f'Total_Score : {totalScore}')

# 정수를 이용한 뺼셈
weight = 90
dietWeight = 77
print('비시즌 몸무게:{}kg'.format(weight))
print('시즌 몸무게:{}kg'.format(dietWeight))
print('총 감량 체중:{}kg'.format(weight-dietWeight))

# *실습* 이번달 알바비와 카드값을 입력하고, 남은 금액이 얼마인지 출력해보자.

partTimeMoney = int(input('이번달 알바비: '))
cardMoney = int(input('이번달 카드값: '))
accountMoney = partTimeMoney - cardMoney

print(f'계좌 잔액 : {accountMoney} 원')