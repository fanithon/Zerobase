# 나눗셈 결과 나머지만 구함

num1 = 10
num2 = 3

result = num1 // num2
print('num1 : {}, num2 : {}, result = {}'.format(num1,num2,result))

# 나머지와 몫을 한번에 구하기
result = divmod(num1, num2)
print('result : {}'.format(result))
print('몫: {}'.format(result[0]))
print('나머지: {}'.format(result[1]))


# 실습
'''
- 학급 전체 학생 수 입력
- 한 모둠에 속하는 학생 수 입력
- 전체 모둠 수와 남는 학생 수 출력
'''

# allStu = int(input('학급 전체 학생 수 : '))
# groupStu = int(input('한 모둠에 속하는 학생 수 :'))
# result1 = divmod(allStu,groupStu)
#
# print('학급 전체 학생 수 : {}'.format(allStu))
# print('한 모둠에 속하는 학생 수 : {}'.format(groupStu))
# print('전체 모둠 수 : {}'.format(result1[0]))
# print('남는 학생 수 : {}'.format(result1[1]))

# 실습
'''
-123개의 사과를 4개씩 직원들한테 나누어 주려고한다. 최대 나누어 줄 수 있는 직원의
수와 남는 사과 개수를 출력해보자. 
'''

apple = 123
divide = 4
appleResult = apple // divide
namApple = apple % divide

print('전체 사과의 개수 : {}'.format(apple))
print('나누어 주는 사과의 개수 : {}'.format(divide))
print('최대 나누어 줄 수 있는 직원의 수 : {}명'.format(appleResult))
print('남는 사과의 개수 : {}개'.format(namApple))



