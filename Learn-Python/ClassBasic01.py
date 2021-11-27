class Person:
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.likes = {'coffee':['스타벅스', '엔젤리너스', '이디야'],
                      'hobby':['낚시', '등산', '골프']}
        pass

    def printPerson(self):
        print(F'이름 = {self.name}, 나이 = {self.age}')
        pass
    pass
    
p1 = Person('홍길동', 25)
p2 = Person('김청수', 24)
print(f'이름 = {p1.name}, 나이 = {p1.age}')
print(f'이름 = {p2.name}, 나이 = {p2.age}')
p1.printPerson()
p2.printPerson()

p3 = Person('내친구', 26)
print(F'이름 = {p3.name}, 나이 = {p3.age}, 가장 좋아하는 커피 = {p3.likes["coffee"][2]}, 가장 즐겨하는 취미 = {p3.likes["hobby"][2]}')
# 이름 = 내친구, 나이 = 26, 가장 좋아하는 커피 = 이디야, 가장 즐겨하는 취미 = 골프



