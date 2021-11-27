# ================================================================================================================================
# < 파이썬 스코프와 이름공간 >
# 이름 공간은 이름에서 객체로 가는 매핑입니다. 대부분의 이름 공간은 현재 파이썬 딕셔터리로 구현되어 있지만, 보통 다른 식으로는 알아차릴 수 없다.
# 
# 1. 전역 네임 스페이스 : 모듈별로 존재하며, 모듈 전체에 통용되는 이름을 사용한다.
# 2. 지역 네임 스페이스 : 함수 및 메소드 별로 존재하며, 함수 내의 지역 변수들이 소속된다.
# 3. 빌트인 네임 스페이스 : 기본 내장 함수 및 기본 예외들의 이름을 저장하는 곳
# 4. 어떤 의미에서 객체의 어트리뷰트 집합도 이름 공간을 형성한다.
# 
# 스코프는 이름 공간을 직접 엑세스할 수 있는 파이썬 프로그램의 텍스트 적인 영억이다.
# 스코프가 정적으로 결정됨에도 불구하고, 동적으로 사용된다. 실행 중 어느 시점에서건, 이름 공간을 직접 엑세스 가능한, 세 개나 네 개의 중첩된 스코프가 있다.
# 1. 가장 먼저 검색되는, 가장 내부의 스코프는 지역 이름들을 포함한다.
# 2. 둘러싸고 있는 함수들의 스코프는, 가장 가까이서 둘러싸는 스코프로부터 검색이 시작된다. 비 지역(non-local)이지만 비 전역(non-global)이름들을 포함한다.
# 3. 마지막 직전의 스코프는 현재 모듈의 전역 이름들을 포함한다.
# 4. (가장 나중에 검색되는) 가장 외부의 스코프는 내장 이름들을 포함하고 있는 이름 공간이다.
# 
# global 문은 특정 변수가 전역 스코프에 있으며, 그곳에 재연결되어야 함을 가리킨다.
# nonlocal 문은 특정 변수가 둘러싸는 스코프에 있으며 그곳에 재연결되어야 함을 가리킨다.
# ================================================================================================================================



def scope_test():
    def do_local():
        spam = "local spam"
        
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print(F"After local assignment: {spam}")    # test spam
    do_nonlocal()
    print(F"After nonlocal assignment: {spam}") # nonlocal spam
    do_global()
    print(F"After global assignment: {spam}")   # nonlocal spam
    pass
    
scope_test()
print(F"In global scope: {spam}")               # global spam



class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return 'hello world'
    
    pass

x = MyClass() # 새 인스턴스를 만들고 이 객체를 지역 변수 x에 대입
print(MyClass.i, MyClass.f, MyClass.__doc__) # 12345 <function MyClass.f at 0x0093B220> A simple example class
xf = x.f
print(xf())           # hello world
print(MyClass.f(x))   # hello world

# ================================================================================================================================
# 파이썬에서 메서드 객체는 다음과 같이 저장된 후에 나중에 호출하는 것도 가능하다.
# xf = x.f    <- 변수 xf에 저장
# xf()        <- 호출
# 파이썬에서 메서드의 특별함은 인스턴스 객체가 함수의 첫 번째 인자로 전달된다. 위에서 x.f()는 정확히 MyClass.f(x)와 동일하다
# ================================================================================================================================
class Reservation:
    def __init__(self, opt1, opt2, opt3):
        self.hotel = "APA 호텔 롯폰기 식스"
        self.WIFI = True
        self.star = 3
        self.sPeriod = '20211114'
        self.ePeriod = '20211121'
        self.roomOption = [opt1, opt2, opt3]
    
    
    def addOption(self, optName):
        self.roomOption.append(optName)
        
    def removeOption(self, optName):
        self.roomOption.remove(optName)
    
x = Reservation('싱글베드 2개', '금연', '샤워실&욕조')
print(F"호텔이름 {x.hotel}, 와이파이 {x.WIFI}, 별점 {x.star}, 머무는 기간 {x.sPeriod, x.ePeriod}, \
    옵션 {x.roomOption[0], x.roomOption[1], x.roomOption[2]}")

x.addOption('라면서비스')
print(x.roomOption)
x.removeOption('금연')
print(x.roomOption)



# ================================================================================================================================
# < 클래스 변수와 인스턴스 변수 >
# 일반적으로 인스턴스 변수는 인스턴스별 데이터를 위한 것이고 클래스 변수는 그 클래스의 모든 인스턴스에서 공유되는 어트리뷰트와 메서드를 위한 것이다.
# 클래스 어트리뷰트인 모든 함수는 그 클래스의 인스턴스들을 위한 메서드를 정의한다. 그리고 함수 정의가 클래스 정의에 텍스트 적으로 둘러싸일 필요는 없다.
# ================================================================================================================================

class Dog:
    kind = 'canine'
    
    def __init__(self, name):
        self.name = name

dogA = Dog('Fido')
dogB = Dog('Buddy')
print(dogA.kind, dogB.kind, dogA.name, dogB.name) # canine canine Fido Buddy




def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    
    h = g

# f, g, h는 모두 함수 객체를 가리키는 클래스 C의 어트리뷰트고, 결과적으로 이것들은 모두 C의 인스턴스들의 메서드이다.
# h는 g와 정확히 동등하다. 그러나 이런 방식은 잘 안 쓴다.
cTest = C()
print(F"""
      f함수 = {cTest.f(10, -8)}, g함수 = {cTest.g()}, h함수 = {cTest.h()}
      """)

# 메서드는 일반 함수들과 마찬가지로 전역 이름을 참조할 수 있다.
# 메서드에 결함한 전역 스코프는 그것의 정의를 포함하는 모듈입니다.
# 메서드에서 전역 데이터를 사용할 좋은 이유는 거의 없다. 그러나 전역 스코프에 정의된 함수와 메서드 뿐만 아니라, 
# 그곳에 임포트된 함수와 모듈도 메서드가 사용할 수 있다





