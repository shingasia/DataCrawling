# 서브디렉터리에서 가져오기
from modules.sub1.sub2 import MenuSelect as menus # sub2 디렉터리의 MenuSelect.py 파일을 menus라는 별칭을 부여
from modules.sub1.fibo import fib as fiboncci1, fib2 as fibonacci2 # fibo.py에 있는 모든 것
from modules.sub3.calc import *     # calc.py에 있는 모든 것
from modules.sub3.sj import *       # sj.py에 있는 모든 것

fiboncci1(1000)
result = fibonacci2(2000)
print('result ==> '+str(result))
menus.printOrderList()


addResult = add(3.4, 7.64532)
print(addResult)
subResult = sub(7.3542345, 32.6447530234)
print(subResult)

data = [10, 20, 30, 40, 50]
print(total(data))
print(avg(data))


