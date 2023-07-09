# 조건식(삼항연산자)의 두가지 사용법
#
# userPoint = int(input('유저 포인트 : '))
# minAblePoint = 1000

# # 조건식 결과에 따른 실행만 하는 경우
#
# print('포인트 사용 가능') if userPoint >= minAblePoint else print('포인트 사용 불가')
#
# # 조건식 결과를 변수에 할당하는 경우
# result = '가능' if userPoint >= minAblePoint else '불가능'
# print('포인트 사용 가능 여부: {}'.format(result))

# 조건식을 if ~ else문으로 변경


# # 조건식 결과에 따른 실행
# if userPoint >= minAblePoint:
#     print('포인트 사용 가능')
# else:
#     print('포인트 사용 불가능')
#
# # 조건식 결과를 변수에 할당
#
# if userPoint >= minAblePoint:
#     result = '가능'
# else:
#     result = '불가능'
#
# print('포인트 사용 가능여부 : {}'.format(result))

# 모든 if ~else문을 조건식으로 표현할 수 있는 건 아니다.

# if userPoint >= minAblePoint:
#     result = '가능'
# else:
#     result = '불가능'
#     lackPoint = minAblePoint - userPoint
#     print('포인트가 {}점 부족합니다.'.format(lackPoint))
#
# print('포인트 사용 가능 여부 : {}'.format(result))

# 실습
# 비올 확률을 입력하고 비올 확률이 55% 이상이라면, '우산을 챙기세요' 그렇지 않으면 ' 양산을 챙기세요' 출력

rainPercent = float(input('비올 확률 입력: '))
minRainPercent = 0.55

# if rainPercent >= minRainPercent:
#     print('우산을 챙기세요.')
# else:
#     print('양산을 챙기세요.')

print('우산을 챙기세요.') if rainPercent >= minRainPercent else print('양산을 챙기세요.')


