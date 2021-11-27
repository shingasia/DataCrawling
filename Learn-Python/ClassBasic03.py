class Grade:
    def __init__(self):
        self.kor=90
        self.__eng=77   # 접근제어자
        self.math=95
        pass
    
    def getEng(self):
        return self.__eng

    def setEng(self, eng):
        self.__eng = eng

g1=Grade()
print(g1.math)
# print(g1.__eng)  # 접근불가능

print(g1.getEng()) # 77
g1.setEng(100)
print(g1.getEng()) # 100


class Employee:
    pass

e1 = Employee()
e1.name = 'Emma'
e1.dept = 'Business Computing'
e1.salary = 2_000_000

def printInfo(obj):
    print(F"{obj.name} {obj.dept} {obj.salary}")
e1.introduce = printInfo

print(e1.introduce)
e1.introduce(e1)
print(F"{e1.name} {e1.dept} {float(e1.salary)}")




class Animation:
    
    def __init__(self):
        self.author = '타츠이 유카리'
        self.category = '일본 청춘물'
        self.title = '4월은 너의 거짓말'
        self.broadcast_period = '2021년 ~ 2015년'
    
    def memo(self):
        print("과거 남다른 피아노 연주 실력으로 각종 콩쿠르를 휩쓸었지만 \
            모종의 이유로 지금은 피아노를 멀리하고 있는 소년 피아니스트가 자유롭고 열정적인 음악을 사랑하는 \
            소녀 바이올리니스트와의 만남을 계기로 다시금 피아노와 마주한다")

ani = Animation()
print(ani)
print(ani.memo.__self__)
print(ani.memo.__func__)

# 인스턴스 메서드 객체도 어트리뷰트를 갖는다. m.__self__는 메서드 m()과 결합한 인스턴스 객체이고, m.__func__는 메서드에 상응하는 함수 객체이다.



