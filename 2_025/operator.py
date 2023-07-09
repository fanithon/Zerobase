# 다자택일 조건문
# if ~ elif문


# exampleScore = int(input('시험 성적 입력: '))
# grade = ''
#
# if exampleScore >= 90:
#     grade = 'A'
# elif exampleScore >= 80:
#     grade = 'B'
# elif exampleScore >= 70:
#     grade = 'C'
# elif exampleScore >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
#
# print('성적 : {} \t 학점 : {}'.format(exampleScore, grade))

# 실습
# 계절을 입력하면 영어로 번역되는 프로그램을 만들어보자.

# print('계절 : 봄, 여름, 가을, 겨울')
# seasonStr = input('계절 입력: ')
#
# if seasonStr == '봄':
#     print('{} : {}'.format('봄', 'spring'))
# elif seasonStr == '여름':
#     print('{} : {}'.format('여름', 'summer'))
# elif seasonStr == '가을':
#     print('{} : {}'.format('가을', 'fall'))
# elif seasonStr =='겨울':
#     print('{} : {}'.format('겨울', 'winter'))
# else:
#     print('찾을 수 없는 계절명 입니다.')

# 키오스크에서 메뉴를 선택하면 영수증이 출력되는 프로그램을 제작
print('1.카페라떼(3.5) \t 2. 에스프레소(2.5) \t 3. 아메리카노(3.0)')
userChooseMenu = int(input('메뉴 선택 :'))

print('=' * 20)

if userChooseMenu == 1:
    print('메뉴 : 카페라떼')
    print('가격 : 3,500원')
elif userChooseMenu == 2:
    print('메뉴 : 에스프레소')
    print('가격 : 2,500원')
elif userChooseMenu == 3:
    print('메뉴 : 아메리카노')
    print('가격 : 3,000원')

print('=' * 20)


