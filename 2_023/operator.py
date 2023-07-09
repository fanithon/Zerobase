# # 양자택일 조건문
# # if ~ else문 : 조건식 결과에 따라 둘 중에 하나가 실행됨.
#
# passScore = 80
# myScore = int(input('점수 입력: '))
#
# if myScore >= passScore:
#     print("Pass !")
#
# else:
#     print("Fail")

# pass 키워드
# messageString = input('메시지를 입력하시오. : ')
#
# if len(messageString) >= 500:
#     pass
# else:
#     pass

# 실습

# # 나이가 65세 이상이면 교통 요금 무료를 적용하는 프로그램을 제작
#
# seniorAge = 65
#
# passengerAge = int(input('나이 입력 : '))
#
# if passengerAge >= seniorAge:
#     print('경로 우대. 무료로 대중교통을 이용 가능합니다.')
# else:
#     print('교통 요금을 지불하세요.')

# 소수점 첫 번째 자리에서 반올림 하는 프로그램을 제작

floatNum = float(input('소수 입력 : '))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum)+1))
else:
    print('버림 : {}'.format(int(floatNum)))
