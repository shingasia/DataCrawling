def fibonacci(num):
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a+b
        pass
    print()

fibonacci(3000)

def fibonacci2(num):
    """ Return a list containing the Fibonacci series up to n. """ # 도큐멘테이션 문자열
    result = []
    a, b = 0, 1
    while a<num:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fibonacci2(100)
print(f100)
print(fibonacci) # <function fibonacci at 0x0148B148>

# ================================================================================================
# return 문은 함수로부터 값을 갖고 복귀하게 만듭니다. 표현식 인자 없는 return 은 None을 돌려줍니다.
# 함수의 끝으로 도달하면 역시 return 문을 생략해도 None을 돌려줍니다.
# ================================================================================================

# 함수의 디폴트 매개 변수 (기본 인자 값)
def average1(num1, num2, other_numbers=[10, 20, 30]):
    if len(other_numbers) == 0:
        return (num1+num2)/2
    result = 0
    for n in other_numbers:
        result += n
    return (result+num1+num2)/(len(other_numbers)+2)

print(average1(50, 55, [7, 7, 7, 7])) # 22.166666666666668
print(average1(100, 200))             # 72.0 <- 결과가 이상함에 주의!!!

# < 중요한 주의사항 > ============================================================================================
# 함수의 기본값은 오직 한 번만 값이 구해집니다. 이것은 기본값이 리스트, 딕셔터리, 대부분 클래스의 인스턴스와 같이
# 가변 객체일 때 차이를 만든다. 예를 들어 다음 함수는 계속되는 호출로 전달된 인자들을 누적한다.
#    def f(a, L=[]):
#        L.append(a)
#        return L
#    print(f(1)) => [1]
#    print(f(2)) => [1, 2]
#    print(f(3)) => [1, 2, 3]
# ================================================================================================================


# 키워드 인자 -> 함수는 kwarg=value 형식의 키워드 인자를 사용해서 호출될 수 있다.
def employeeComponent(position, empCode='E00001', age=25, name='olivia'):
    print(f'사원코드 = {empCode}, 나이 = {age}, 이름 = {name}, 직책 = {position}')

employeeComponent(None, empCode='E0005', age=31, name='charlotte') # 사원코드 = E0005, 나이 = 31, 이름 = charlotte, 직책 = None
# employeeComponent() # Error 기본 인자 값이 없다.
employeeComponent('대리')                                          # 사원코드 = E00001, 나이 = 25, 이름 = olivia, 직책 = 대리
employeeComponent(empCode='S00010', name='Sera', position='사원')  # 사원코드 = S00010, 나이 = 25, 이름 = Sera, 직책 = 사원
# 인자를 kwarg=value 형식으로 다 넘겨주면 파라미터 순서는 관계 없다.
employeeComponent('팀장', 'T00002', 35, name='isabella')           # 사원코드 = T00002, 나이 = 35, 이름 = isabella, 직책 = 팀장
# 위치 인자와 키워드 인자를 같이 사용하려면 키워드 인자는 위치 인자 보다 뒤에 나와야 한다.

# 함수 인자 넘겨줄 때 주의사항
# ================================================================================================
# 1. 위치 인자의 값은 함수의 기본 인자 값이 없으면 무조건 넘겨줘야 한다. (생략 불가)
# 2. 함수의 파라미터가 기본 인자값이 없어도 kwarg=value 형태의 키워드 인자로 호출하면 키워드인자 순서와 함수에 정의된 파라미터 순서는 일치할 필요가 없다.
# 3. 위치 인자와 키워드 인자를 같이 사용하려면 키워드 인자는 위치 인자 보다 뒤에 나와야 한다.
# ================================================================================================

# 특수 매개 변수( / 와 * )
# def function_name(pos1, pos2, ..., /, pos_or_kwd1, pos_or_kwd2, ..., *, kwd1, kwd2, ...):
# 함수 정의에 매개변수를 위치 전용(Positional Only), 위치-키워드(Positional or Keyword), 키워드 전용(Keyword Only)로 표시할 수 있다.
# '/' 앞에는 위치 전용 매개변수로 인자 값의 순서가 중요하고, '/' 다음의 매개변수는 위치-키워드 또는 키워드 전용일 수 있다.

def pos_only_arg(arg1, arg2, arg3='arg3', /): # 위치 인자만 사용하게 끔 하려면 이렇게 하면 된다.
    print(arg1, arg2, arg3)

def kwd_only_arg(*, kwd1, kwd2, kwd3):        # 키워드 인자만 사용하게 끔 하려면 이렇게 하면 된다.
    print(kwd1, kwd2, kwd3)

def mixed_arg(pos_only1, pos_only2, /, pos_or_kwd1, pos_or_kwd2, pos_or_kwd3, *, kwd_only1, kwd_only2):
    print("pos_only1 = {pos_only1}, pos_only2 = {pos_only2}, pos_or_kwd1 = {pos_or_kwd1}, pos_or_kwd2 = {pos_or_kwd2}, pos_or_kwd3 = {pos_or_kwd3}, \
        kwd_only1 = {kwd_only1}, kwd_only2 = {kwd_only2}".format(pos_only1=pos_only1, pos_only2=pos_only2, pos_or_kwd1=pos_or_kwd1, pos_or_kwd2=pos_or_kwd2, pos_or_kwd3=pos_or_kwd3, \
        kwd_only1=kwd_only1, kwd_only2=kwd_only2))
    pass



pos_only_arg(100, 200, 300)
kwd_only_arg(kwd2='kwd2', kwd3='kwd3', kwd1='kwd1')
mixed_arg('위치1', '위치2', '위치키워드1', kwd_only2='키워드2', kwd_only1='키워드1', pos_or_kwd3='위치키워드3', pos_or_kwd2='위치키워드2')

# < 위치 인자와 키워드 인자를 각각 튜플과 딕셔너리로 인자 받기 >============================================================
# def function_name(value1, value2, ..., *positions, **keywords):
# *positions는 형식 매개변수에 대응하지 않은 위치 인자들을 튜플로 받는다.
# **keywords는 형식 매개변수에 대응하지 않은 키워드 인자들을 딕셔터리로 받는다.
# *positions는 **keywords 앞에 나와야 한다.
# ==========================================================================================================================

def packing_icecream(size='쿼터', *kind, **others):
    for taste in kind:
        print(taste, end=', ')
        pass
    print() # 줄바꿈
    for key, taste in others.items():
        print(f'{key} = {taste}')
        pass
    print(F"사이즈는 {size}입니다.")
    pass
packing_icecream('Family','골든 애플 요거트', '너는 참 달고나', '망고탱고',
t1='파핑파핑 바나나', t2='레드 라즈베리 소르베', t3='아이스 맥심 모카골드', t4='베리베리 스트로베리', t5='이상한 나라의 솜사탕')



# 람다 표현식 (lambda 키워드를 사용해서 작고 이름 없는 함수를 만들 수 있다)
lambdaF = lambda x, y : x**y
print(lambdaF(3, 4)) # 81









