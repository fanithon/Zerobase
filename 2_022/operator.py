# if문

if 10 > 5:
    print('10은 5보다 크다.')

num1 = 10
num2 = 20

if num1 < num2 :
    print('num1은 num2보다 크지 않다.')

# 실습
# 국어, 영어, 수학 점수를 입력하고 평균이 90점 이상이면 '참 잘했어요.'를 출력

# korScore = int(input('국어 점수: '))
# engScore = int(input('영어 점수: '))
# mathScore = int(input('수학 점수: '))
# totalSCore = korScore + engScore + mathScore
# averageScore = totalSCore / 3
#
# print('평균 :  %.2f ' % averageScore)
# if averageScore >= 90:
#     print('참 잘했어요.')

# 실습 2
# 실내 온도를 입력 후 온도가 28도 이상이면 '냉방 작동!' 출력 / 20 이하면 '난방 작동'

highTemp = 28
lowTemp = 20

innerTemp = int(input('실내 온도를 입력하세요 :'))

if innerTemp >= highTemp:
    print('냉방 작동 !')

if innerTemp <= lowTemp:
    print('난방 작동 !')


