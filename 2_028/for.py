# 반복문
#
# num1 = int(input('원하는 단수를 입력하세요:'))
# print('구구단 {}단 출력'.format(num1))
#
# for i in range(1,10):
#     print('{} * {} = {}'.format(num1, i, (num1*i)))

# 반복문 종류

# 횟수에 의한 반복 - 지정 횟수만큼 반복 실행
for i in range(100):
    print('i ->{}'.format(i))

# 조건에 의한 반복 - 조건에 만족할 때까지 반복 실행
num1 = 0
while (num1 < 10):
    print('num1 -> {}'.format(num1))
    num1 += 1

