class Person:
    def __init__(self):
        self.name = input('이름: ')
        self.age = int(input('나이: '))
        pass
    
    def printPerson(self):
        print("name = {name}, age = {age}".format(name=self.name, age=self.age))
        pass

pList = []

for i in range(3):
    pList.append(Person())

for i in pList:
    i.printPerson()