books = ['일반화학', '물리학 기초1', '전자기학', '컴퓨터구조론']

for a in books:
    print(a, len(a))

# 파이썬의 for문은 임의의 시퀀스의 항목들을 순서대로 이터레이션한다.

# range(start, stop[, step])
for a in range(1, 20, 2):
    print(a, end=" ")

icecream = ['아이스 맥심 모카골드', '오레오 쿠키 앤 카라멜', '파핑파핑 바나나', '레드 라즈베리 소르베', '골든 애플 요거트', '너는 참 달고나']
for a in range(len(icecream)):
    print(a, icecream[a])


# ▶▶▶▶▶ Python의 이터러블 객체, 이터레이터, 시퀀스, 제너레이터에 대해 쭉 읽어보면 도움이 된다.

for n in range(2, 30): # 2이상 30미만의 소수 찾기
    for x in range(2, n):
        if n%x == 0:
            print(n, ' equals ', x, '*', n//x)
            break
    else: # 여기서 else는 if 문이 아니라 for 루프에 속한다.
        print(n, ' is a prime number')

# ================================================================================================================================
# try 문의 else 절은 예외가 발생하지 않을 때 실행되고, 루프의 else 절은 break가 발생하지 않을 때 실행된다.
# Python에서는 루프 문은 else절을 가질 수 있다. 루프가 이터러블의 소진이나(for의 경우) 조건이 거짓이 돼서 (while의 경우) 종료할 때 실행된다.
# break 문으로 종료할 때는 else절은 실행되지 않는다.
# ================================================================================================================================

for num in range(2, 20):
    if num%2 == 0:
        print('2의 배수를 찾았다.', num)
        continue
    print('홀수입니다.')


for (first, second) in [('치킨', 15000), ('피자', 17000), ('아이스크림', 11000),]:
    print(first, second, end=' AND ')


# pass 문은 아무것도 하지 않는다. 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 사용할 수 있다.
"""
while True:
    pass

class MyEmptyClass:
    pass

def initlog(*args, **kwargs):
    pass
"""

