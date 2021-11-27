# @classmethod, @staticmethod, @abstractmethod 등등 알아보기

class Computer:
    def toString(self):
        print(F'{self.cpu} {self.ram} {self.disk} {self.power}')
        pass
    pass

a = Computer()

a.cpu='Intel i9 10th'
a.ram='16GB'
a.disk='2TB'
a.power=False


a.toString()

def powerOnOff(obj):
    if(obj.power):
        obj.power=False
    else:
        obj.power=True

a.powerOnOff = powerOnOff
a.powerOnOff(a)

a.toString()
print(a.__init__)
print(a.__class__)

