# 비교 연산자
# 숫자 비교
num1 = 10 ; num2 = 5

result = num1 > num2
print('num1 > num2 : {}'.format(result))
result = num1 >= num2
print('num1 > num2 : {}'.format(result))
result = num1 < num2
print('num1 > num2 : {}'.format(result))
result = num1 <= num2
print('num1 > num2 : {}'.format(result))
result = num1 == num2
print('num1 > num2 : {}'.format(result))
result = num1 != num2
print('num1 > num2 : {}'.format(result))

# 실습
#숫자 두 개를 입력한 후 비교 연산 결과를 출력하는 코드를 작성하자.
userInputNumber1 = int(input('첫 번째 숫자를 입력 : '))
userInputNumber2 = int(input('첫 번째 숫자를 입력 : '))

print('{} > {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 > userInputNumber2)))
print('{} >= {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 >= userInputNumber2)))
print('{} < {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 < userInputNumber2)))
print('{} <= {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 <= userInputNumber2)))
print('{} == {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 == userInputNumber2)))
print('{} != {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 != userInputNumber2)))


# 실습2
# 자동차의 전장과 전폭을 입력하면 자동차 기계 세차 가능여부를 출력하는 코드를 작성
# (최대 전장 길이 : 5200mm, 최대 전폭 길이 : 1985mm )

maxLength = 5200
maxWidth = 1985

myCarLength = int(input('전장 길이 입력 : '))
myCarWidth = int(input('전폭 길이 입력 : '))

print('전장 가능 여부 : {}'.format(myCarLength <= maxLength))
print('전폭 가능 여부 : {}'.format(myCarWidth <= maxWidth))
