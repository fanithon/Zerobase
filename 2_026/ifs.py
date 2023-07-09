# 다자택일 사용시 주의할 점
 # 조건식 순서가 중요하다.

 # 실습
 # 자동차 배기량에 따라 세금을 부과한다고 할 때, 다음 표에 맞는 세금 출력 프로그램

carDisplacement = int(input('자동차 배기량 : '))

if carDisplacement >= 5000:
     print('세금 : 600,000원')
elif carDisplacement >= 4000 and carDisplacement < 5000:
     print('세금 : 500,000원')
elif carDisplacement >= 3000 and carDisplacement < 4000:
     print('세금 : 400,000원')
elif carDisplacement >= 2000 and carDisplacement < 3000:
     print('세금 : 300,000원')
elif carDisplacement >= 1000 and carDisplacement < 2000:
     print('세금 : 200,000원')
elif carDisplacement < 1000:
     print('세금 : 100,000원')
