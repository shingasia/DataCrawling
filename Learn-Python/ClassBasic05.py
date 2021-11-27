class Phone:
    
    phone_name = '피쳐폰'
    
    def __init__(self, p_number, p_name):
        print('Phone 생성자 호출')
        self.p_number = p_number
        self.p_name = p_name
    
    # super().__init__()
    # super(ClassName, self).__init__()
    # super().__init__(**kwargs)
    # super(ClassName, self).__init__(**kwargs)
        
    
    def call(self, number):
        print(f'Phone 전화걸기 -> {number}')
        
    def send_msg(self, number, msg):
        print(f'Phone 메세지 보내기 : {number, msg}')
    
    def get_info(self):
        print(f'Phone 내 번호 : {self.p_number}')
        print(f'Phone 내 이름 : {self.p_name}')


class ApplePhone(Phone):
    
    def __init__(self, a_number, a_name):
        super(ApplePhone, self).__init__(a_number, a_name) # 이 표현은 파이썬 2.x 문법이다. 3.x에서도 사용가능
        print('ApplePhone 생성자 호출')
        
    def button_home(self):
        print('ApplePhone 홈 버튼 눌림')
        

class GalaxyPhone(Phone):
    
    def __init__(self, g_number, g_name):
        super(GalaxyPhone, self).__init__(g_number, g_name)
        print('GalaxyPhone 생성자 호출')
    
    def button_cancel(self):
        print('GalaxyPhone 취소(뒤로가기) 버튼이 눌렸습니다')

phone = Phone('010-1111-1111', 'Sera')
apple = ApplePhone('010-2222-2222', 'Lena')
galaxy = GalaxyPhone('010-3333-3333', 'Elsa')

phone.get_info()
apple.get_info()
galaxy.get_info()

apple.button_home()      # ApplePhone 홈 버튼 눌림
galaxy.button_cancel()   # GalaxyPhone 취소(뒤로가기) 버튼이 눌렸습니다


print("\n".join([f'apple.phone_name => {apple.phone_name}', f'galaxy.phone_name => {galaxy.phone_name}', f'Phone.phone_name => {Phone.phone_name}', f'ApplePhone.phone_name => {ApplePhone.phone_name}', f'GalaxyPhone.phone_name => {GalaxyPhone.phone_name}']))
"""
apple.phone_name => 피쳐폰
galaxy.phone_name => 피쳐폰
Phone.phone_name => 피쳐폰
ApplePhone.phone_name => 피쳐폰
GalaxyPhone.phone_name => 피쳐폰
"""

print(ApplePhone.__mro__) # (<class '__main__.ApplePhone'>, <class '__main__.Phone'>, <class 'object'>)
print(GalaxyPhone.__mro__)# (<class '__main__.GalaxyPhone'>, <class '__main__.Phone'>, <class 'object'>)
print(ApplePhone.mro())   # [<class '__main__.ApplePhone'>, <class '__main__.Phone'>, <class 'object'>]
print(GalaxyPhone.mro())  # [<class '__main__.GalaxyPhone'>, <class '__main__.Phone'>, <class 'object'>]
print(issubclass(ApplePhone, object)) # True
print(issubclass(GalaxyPhone, Phone)) # True
print(isinstance(apple, object))      # True
print(isinstance(apple, ApplePhone))  # True


class Parent:
    
    def __init__(self, p1, p2):
        '''super()를 사용하지 않으면 overriding 됩니다.'''
        self.p1 = p1
        self.p2 = p2
            

class Child(Parent):
    
    def __init__(self, c1, **kwargs):
        
        super().__init__(kwargs['p1'], kwargs['p2']) # super(Child, self).__init__(kwargs['p1'], kwargs['p2']) 와 같다
        self.c1 = c1
        self.arg1 = kwargs['arg1']
        self.arg2 = kwargs['arg2']
        
child = Child(p1="This is Parent's p1", p2="This is Parent's p2", c1="This is Child's c1", arg1="argument1", arg2="argument2", arg3="others...")

print(F"{child.p1}, {child.p2}, {child.c1}, {child.arg1}, {child.arg2}") # This is Parent's p1, This is Parent's p2, This is Child's c1, argument1, argument2













# ================================================================================================================================
# 인스턴스의 형을 검사하려면 isinstance() 를 사용합니다: isinstance(obj, int) 는 obj.__class__ 가 int 거나 int 에서 파생된 클래스인 경우만 True 가 됩니다.
# 클래스 상속을 검사하려면 issubclass() 를 사용합니다: issubclass(bool, int) 는 True 인데, bool 이 int 의 서브 클래스이기 때문입니다. 하지만, issubclass(float, int) 는 False 인데, float 는 int 의 서브 클래스가 아니기 때문입니다.
# ================================================================================================================================


# ================================================================================================================================
# class super([type[, object-or-type]])
# type의 부모나 형제 클래스에 위임하는 프락시 객체를 돌려준다. 이는 클래스에서 재정의된 상속된 메서드를 엑세스할 때 유용하다
# object-or-type은 검색할 메서드 결정 순서를 결정한다.
# 예를 들어, object-or-type의 __mro__가 D -> B -> C -> A -> object이고 type의 값이 B이면, super()는 C -> A -> object를 검색한다.
# object-or-type의 __mro__어트리뷰트는 메서드 결정 검색 순서를 나열하는데 getattr()과 super()에서 사용된다. 이 어트리뷰트는 동적이며 상속 계층 구조가 변경될 때마다 바뀔 수 있다.
# class.__mro__ : 이 어트리뷰트는 메서드 결정 중에 베이스 클래스를 찾을 때 고려되는 클래스들의 튜플
# class.mro()   : 이 메서드는 인스턴스의 메서드 결정 순서를 사용자가 정의하기 위해 메타 클래스가 재정의할 수 있다. 클래스 인스턴스를 만들때 호출되며, 그 결과는 __mro__어트리뷰트에 저장된다.
# ================================================================================================================================

# ================================================================================================================================
# 두 번째 인자가 생략되면, 반환되는 슈퍼 객체는 연결되지 않았습니다(unbound)
# 두 번째 인자가 객체면, isinstance(obj, type)은 참이어야 한다.
# 두 번째 인자가 형(type)이면, issubclass(type2, type)은 참이어야 한다. (클래스 메서드에 유용)
# ================================================================================================================================





