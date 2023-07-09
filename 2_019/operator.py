# 비교 연산자
# 문자비교 : 아스키코드를 이용한 비교 연산

cha1 = "A"  # 65
cha2 = "S"  # 83

print('\'{}\' > \'{}\' : {}'.format(cha1, cha2, (cha1 > cha2)))
print('\'{}\' >= \'{}\' : {}'.format(cha1, cha2, (cha1 >= cha2)))
print('\'{}\' < \'{}\' : {}'.format(cha1, cha2, (cha1 < cha2)))
print('\'{}\' <= \'{}\' : {}'.format(cha1, cha2, (cha1 <= cha2)))
print('\'{}\' == \'{}\' : {}'.format(cha1, cha2, (cha1 == cha2)))
print('\'{}\' != \'{}\' : {}'.format(cha1, cha2, (cha1 != cha2)))


# 문자와 아스키 코드 변환
# ord() : 문자를 십진수(정수)로 표현
# chr() : 십진수(정수)를 문자로 표현

print('\'A \' -> {}'.format(ord('A')))
print('\'S \' -> {}'.format(ord('S')))

print(' 65 -> {}'.format(chr(65)))
print(' 83 -> {}'.format(chr(83)))

# 문자열 비교 : 문자열 자체를 비교
str1 = 'Hello'
str2 = "hello"

print('{} = {} : {}'.format(str1, str2, (str1 == str2)))
print('{} = {} : {}'.format(str1, str2, (str1 != str2)))

# 알파벳을 입력하면 아스키 코드를 출력하는 코드를 작성하라
alphabetInput = input('알파벳을 입력:')
print('입력한 알파벳 : \'{}\' -> 변환 된 알파벳 : {}'.format(alphabetInput, ord(alphabetInput)))

# 아스키 코드를 입력하면 문자를 출력하도록 코드를 작성하자
asciCodeInput = int(input('아스키 코드 입력 :'))
print('{}: {}'.format(asciCodeInput, chr(asciCodeInput)))