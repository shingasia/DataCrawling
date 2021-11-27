grade=float(input("본인의 학점을 입력하세요 : "))

if grade < 1.8 :
    print('학사경고')
elif grade < 2.5 :
    print('멘토 교수와 면담')
elif grade < 3.5:
    print('분발하시오')
elif grade < 4.2:
    print('열심히 하는 사람')
else:
    print('장학생입니다.')
    if grade > 4.4:
        print('학과장 추천 장학금이 추가로 지급됩니다.')

distance = int(input('거리를 Km 단위로 입력 :'), base=10)
if distance > 100:
    print('비행기')
elif 10 <= distance <= 40:
    print('버스 또는 지하철')
elif distance < 5:
    print('걸어갈 수 있는 거리')
else:
    print('자차 이용')


