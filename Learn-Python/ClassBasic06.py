class A:
    def m(self):
        print("In Class A")
        super().m()

class B:
    def m(self):
        print("In Class B")
        super().m()

class C:
    def m(self):
        print("In Class C")
        # super().m()

class X(A, B):
    def m(self):
        print("In Class X")
        super().m()

class Y(B, C):
    def m(self):
        print("In Class Y")
        super().m()

class Z(X, Y, B):
    def m(self):
        print("In Class Z")
        super().m()

print(Z.__mro__) # (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(Z.mro())   # [<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
a = Z.mro()
a[1], a[2] = a[2], a[1]
print(a)         # [<class '__main__.Z'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]


obj = Z()
obj.m()
# 결과 =========================
# In Class Z
# In Class X
# In Class A
# In Class Y
# In Class B
# In Class C
# ==============================

class Red:
    def printColor(self):
        print("Color is ==> Red")
        super().printColor()
        
class Green:
    def printColor(self):
        print("Color is ==> Green")
        super().printColor()

class Blue:
    def printColor(self):
        print("Color is ==> Blue")
        super().printColor()

class Yellow:
    def printColor(self):
        print("Color is ==> Yellow")
        super().printColor()

class Black:
    def printColor(self):
        print("Color is ==> Black")
        super().printColor()




class Drawing1(Red, Yellow, Black):
    def printColor(self):
        print("Drawing is ==> Drawing1")
        super().printColor()

class Drawing2(Red, Blue, Yellow):
    def printColor(self):
        print("Drawing is ==> Drawing2")
        super().printColor()

class Drawing3(Green, Blue, Black):
    def printColor(self):
        print("Drawing is ==> Drawing3")
        super().printColor()


class Drawing4(Green, Blue, Yellow, Black):
    def printColor(self):
        print("Drawing is ==> Drawing4")
        super().printColor()




class WallPaper1(Drawing1, Drawing2, Drawing3):
    def printColor(self):
        print("WallPaper is ==> WallPaper1")
        super().printColor()

class WallPaper2(Drawing2, Drawing3, Drawing4):
    def printColor(self):
        print("WallPaper is ==> WallPaper2")
        super().printColor()
        
class WallPaper3(Drawing2, Drawing3, Green):
    def printColor(self):
        print("WallPaper is ==> WallPaper3")
        super().printColor()



class MyRoom(WallPaper1, WallPaper2, WallPaper3):
    def printColor(self):
        print("MyRoom ....")
        super().printColor()



print(MyRoom.__mro__)
# (<class '__main__.MyRoom'>, <class '__main__.WallPaper1'>, <class '__main__.Drawing1'>, <class '__main__.WallPaper2'>, <class '__main__.WallPaper3'>, <class '__main__.Drawing2'>, <class '__main__.Red'>, <class '__main__.Drawing3'>, <class '__main__.Drawing4'>, <class '__main__.Green'>, <class '__main__.Blue'>, <class '__main__.Yellow'>, <class '__main__.Black'>, <class 'object'>)
print(MyRoom.mro())
# [<class '__main__.MyRoom'>, <class '__main__.WallPaper1'>, <class '__main__.Drawing1'>, <class '__main__.WallPaper2'>, <class '__main__.WallPaper3'>, <class '__main__.Drawing2'>, <class '__main__.Red'>, <class '__main__.Drawing3'>, <class '__main__.Drawing4'>, <class '__main__.Green'>, <class '__main__.Blue'>, <class '__main__.Yellow'>, <class '__main__.Black'>, <class 'object'>]
room = MyRoom()
room.printColor()

# 결과 =========================
# MyRoom ....
# WallPaper is ==> WallPaper1
# Drawing is ==> Drawing1
# WallPaper is ==> WallPaper2
# WallPaper is ==> WallPaper3
# Drawing is ==> Drawing2
# Color is ==> Red
# Drawing is ==> Drawing3
# Drawing is ==> Drawing4
# Color is ==> Green
# Color is ==> Blue
# Color is ==> Yellow
# Color is ==> Black
# ==============================

# 파이썬3은 mro(Method Resolution Order) 알고리즘은  C3 Linearization 에 대해 알아보자