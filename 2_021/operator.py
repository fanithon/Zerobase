# 조건식
# A if 조건식 else -> 조건식의 결과가 True이면 A실행, 아니면 B실행

num1 = 10
num2 = 100

numResult = True if num1 > num2 else False
print('num1 > num2 : {}'.format(numResult))
print('num1은 num2보다 크다.') if numResult else print('num1은 num2보다 작다.')

# 실습
# # 적설량을 입력하고 적설량이 30mm이상이면 대설 경보를 발령하고
# # 그렇지 않으면 대설 경보를 해제하는 코드를 작성해보자.
#
# snowLimit = 30
# snowAmount = int(input('적설량을 입력:'))
#
# print('적설량 : {}, {}'.format(snowAmount, "대설 경보 발령")) if snowAmount >= snowLimit else \
#     print('적설량 : {}, {}'.format(snowAmount, '대설 경보 해제'))

# 실습
# 국어, 영어, 수학 점수를 입력하면 조건식을 이용해서 과목별 결과와 전체 결과를 출력

# 과목별 합격 점수 60점
# 전체 합격 평균 점수 : 70점
import operator

subjectGoalScore = 60
totalGoalScore = 70

korScore = int(input('국어 점수:'))
engScore = int(input('영어 점수:'))
mathScore = int(input('수학 점수:'))

totalScore = korScore + engScore + mathScore
averageScore = totalScore / 3

# print('국어 점수 : {}, {}'.format(korScore,"국어 합격") if korScore >= subjectGoalScore else print('국어 불합격'))
# print('영어 점수 : {}, {}'.format(korScore,"영어 합격") if engScore >= subjectGoalScore else print('영어 불합격'))
# print('수학 점수 : {}, {}'.format(korScore,"수학 합격") if mathScore >= subjectGoalScore else print('수학 불합격'))
# print('점수 총합: {}, 평균 점수 : {}, {}'.format(totalScore, averageScore, "합격") if totalScore >= totalGoalScore else print('불합격'))

print('국어 점수 : {}, {}'.format(korScore,'Pass') if operator.ge(korScore, subjectGoalScore) else print("국어 : FAIL"))
print('영어 점수 : {}, {}'.format(engScore,'Pass') if operator.ge(engScore, subjectGoalScore) else print("영어 : FAIL"))
print('수학 점수 : {}, {}'.format(mathScore,'Pass') if operator.ge(mathScore, subjectGoalScore) else print("수학 : FAIL"))
print('총점 : {}, 평균 : {}, {}'.format(totalScore,averageScore,'Pass') if operator.ge(averageScore, totalGoalScore) else print("시험 : FAIL"))