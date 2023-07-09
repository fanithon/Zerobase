# 할당 연산자

# 다음표를 참고해서 연간 누적 강수량을 출력해보자.

rain = 0
avgRain = 0

rain += 30
print('1월당 강수량 : {}mm'.format(rain, ','))
rain += 45
print('2월당 강수량 : {}mm'.format(rain, ','))
rain += 47
print('3월당 강수량 : {}mm'.format(rain, ','))
rain += 55
print('4월당 강수량 : {}mm'.format(rain, ','))
rain += 65
print('5월당 강수량 : {}mm'.format(rain, ','))
rain += 100
print('6월당 강수량 : {}mm'.format(rain, ','))
rain += 128
print('7월당 강수량 : {}mm'.format(rain, ','))
rain += 209
print('8월당 강수량 : {}mm'.format(rain, ','))
rain += 204
print('9월당 강수량 : {}mm'.format(rain, ','))
rain += 186
print('10월당 강수량 : {}mm'.format(format(rain, ',')))
rain += 67
print('11월당 강수량 : {}mm'.format(format(rain, ',')))
rain += 25
print('12월당 강수량 : {}mm'.format(format(rain, ',')))

avgRain = rain / 12
print('-'*30)
print('연간 누적 강수량 : {}mm'.format(format(rain, ',')))
print('연 평균 강수량 : {}mm'.format(avgRain))
print('-'*30)
