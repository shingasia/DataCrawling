# operator 함수로서의 표준 연산자
# ==================================================================================================================================
# operator 모듈은 파이썬의 내장 연산자에 해당하는 효율적인 함수 집합을 내보낸다. 예를 들어, operator.add(x, y)는 x+y표현식과 동등하다.
# 많은 함수 이름은 특수 메서드에 사용되는 이름인데, 이중 밑줄이 없다.
# -> 그러나 이전 버전과의 호환성을 위해, 이들 중 많은 것은 이중 밑줄이 있는 변형을 가진다.
# 객체 비교, 논리 연산, 수학 현산 및 시퀀스 연산을 수행하는 범주로 분류된다.
# ==================================================================================================================================

class Card:
    def __init__(self, **kwargs):
        self.account = kwargs['account']
        self.money = kwargs['money']
        self.bank = kwargs['bank']
        self.name = kwargs['name']
    
    def deposit(self, money):
        self.money += money
    
    def withdraw(self, money):
        self.money -= money
    
    def __eq__(self, other): # a == b
        print("__eq__() 메서드 호출")
        if(self.account == other.account):
            return True
        else:
            return False
    
    def __ne__(self, other): # a != b
        print("__ne__() 메서드 호출")
        if(self.account != other.account or self.bank != other.bank \
            or self.money != other.money or self.name != other.name):
            return True
        else:
            return False
    
    def __le__(self, other): # a <= b
        print("__le__() 메서드 호출")
        if(self.money <= other.money):
            return True
        else:
            return False
    
    def __lt__(self, other): # a < b
        print("__lt__() 메서드 호출")
        if(self.money < other.money):
            return True
        else:
            return False
        
    def __ge__(self, other): # a >= b
        print("__ge__() 메서드 호출")
        if(self.money >= other.money):
            return True
        else:
            return False
    
    def __gt__(self, other): # a > b
        print("__gt__() 메서드 호출")
        if(self.money > other.money):
            return True
        else:
            return False
        
    pass


card1 = Card(account=1111111111, money=500000, bank="KB국민은행", name="아무개")
card2 = Card(account=2222222222, money=500000, bank="신한은행", name="옆집개")
card3 = Card(account=2222222222, money=500000, bank="신한은행", name="옆집개")
# print(card1 >= card2)
print(card1 >= card2) # True
print(card1 != card2) # True
print(card1 < card2)  # False
print(card2 == card3) # True
print(card2 != card3) # False


# ==================================================================================================================================
# 이항 산술 연산
# object.__add__(self, other)            == x가 __add__()메서드를 가진 클래스의 인스턴스일 때, 표현식 x+y의 값을 구하기 위해 x.__add__(y)가 호출된다.
# object.__sub__(self, other)            ==> -
# object.__mul__(self, other)            ==> *
# object.__matmul__(self, other)         ==> @
# object.__truediv__(self, other)        ==> /
# object.__floordiv__(self, other)       ==> //
# object.__mod__(self, other)            ==> %
# object.__divmod__(self, other)         ==> divmod()
# object.__pow__(self, other[, modulo])  ==> pow(), **
# object.__lshift__(self, other)         ==> <<
# object.__rshift__(self, other)         ==> >>
# object.__and__(self, other)            ==> &
# object.__xor__(self, other)            ==> ^
# object.__or__(self, other)             ==> |

# 일항 산술 연산
# object.__neg__(self)                   ==> -
# object.__pos__(self)                   ==> +
# object.__abs__(self)                   ==> abs()
# object.__invert__(self)                ==> ~

# 내장 함수
# object.__complex__(self)               ==> complex()
# object.__int__(self)                   ==> int()
# object.__float__(self)                 ==> float()

# 이것 외에도 중요한 그리고 알아야하는 특수메서드, 특수어트리뷰트 들이 여러개 있다.
# https://docs.python.org/ko/3/reference/datamodel.html
