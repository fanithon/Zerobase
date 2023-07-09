# 중첩 조건문
# 조건문 내 또 다른 조건문이 있을 수 있다.


# exampleScore = int(input('점수 입력:'))
# if exampleScore < 60:
#     print('재시험 대상입니다.')
# else:
#     if exampleScore >= 90:
#         print('Grade : A')
#     elif exampleScore >= 80:
#         print('Grade : B')
#     elif exampleScore >= 70:
#         print('Grade : C')
#     elif exampleScore >= 60:
#         print('Grade : D')

#실습
# 출퇴근시 이용하는 교통 수단에 따라 세금을 감면해주는 정책

selectNum = int(input('출퇴근 대상자인가요? 1. Yes / 2. No'))

if selectNum ==1:
    print('교통 수단을 선택하세요.')
    trans = int(input('1.도보,자전거 \t 2.버스,지하철 \t 3.자가용'))

    if trans == 1:
        print('세금 감면 : 5%')
    elif trans ==2:
        print('세금 감면 : 3%')
    elif trans ==3:
        print('세금 감면 : 1%')
elif selectNum ==2:
    print('세금 변동 없습니다.')
else:
    print('번호를 다시 한번 확인해주세요.')