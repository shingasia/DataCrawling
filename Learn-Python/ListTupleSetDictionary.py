Venti_menu = ['유니콘', '딸기크림 초코칩', '말차 초코칩', '민트 크런치', \
    '토피 크런치', '코코밀크', '코코초코', '자바칩']

numbers = [6,5,4,2,7,8,9,3,1,0,4,3,2,1,8,9]

#========================== 1.append(x)
Venti_menu.append('쿠키앤크림') # 끝에 항목 1개 추가
print(Venti_menu)

#========================== 2. extend(iterable)
Venti_menu.extend(['더블에스프레소', '플레인 요거트', '초코']) # 끝에 이터러블의 모든 항목을 덧붙여서 확장
print(Venti_menu)

#========================== 3. insert(i, x)
Venti_menu.insert(-3, '블루레몬') 
# 주어진 위치(index)에 항목을 삽입한다. a.insert(0, x)는 리스트의 처음에 삽입, insert(len(a), x)는 a.append(x)와 동등하다
print(Venti_menu)

#========================== 4. remove(x)
numbers.remove(1+1) # x와 같은 첫 번째 항목을 삭제 없으면 ValueError
print(numbers) # [6, 5, 4, 7, 8, 9, 3, 1, 0, 4, 3, 2, 1, 8, 9]

#========================== 5. pop([i])
# 주어진 위치에 있는 항목을 삭제하고 그 항목을 돌려준다. 인덱스를 지정하지 않으면 마지막 항목을 삭제하고 돌려준다
numbers.pop(-5) # 3이 삭제됨
print(numbers)  # [6, 5, 4, 7, 8, 9, 3, 1, 0, 4, 2, 1, 8, 9]
numbers.pop(4)  # 8이 삭제됨
print(numbers)  # [6, 5, 4, 7, 9, 3, 1, 0, 4, 2, 1, 8, 9]
numbers.pop()   # 9가 삭제됨
print(numbers)  # [6, 5, 4, 7, 9, 3, 1, 0, 4, 2, 1, 8]

#========================== 6. clear()
# 리스트의 모든 항목을 삭제 del a[:]와 동등
numbers.clear()
print(numbers) # []

#========================== 7. count(x)
# 리스트에서 x가 등장하는 횟수를 돌려준다.
print([1,4,3,2,5,4,2,1,3,4,2,4,3,1,1,2,3,4].count(4)) # 5

#========================== 8. sort(*, key=None, reverse=False)
# 리스트의 항목들을 제자리에서 정렬
numbers = [1,4,3,2,5,4,2,1,3,4,2,4,3,1,1,2,3,4]
numbers.sort()
print(numbers) # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5]

alphabet = ['f', 'e', 'a', 'd', 'q', 'o', 's', 'e', 'b', 's', 'z', 'x', 'x', 'w', 'l', 'L', 'A']
alphabet.sort(reverse=True)
print(alphabet) # ['z', 'x', 'x', 'w', 's', 's', 'q', 'o', 'l', 'f', 'e', 'e', 'd', 'b', 'a', 'L', 'A']

#========================== 9. reverse()
# 리스트의 요소들을 제자리에서 뒤집는다.

#========================== 10. copy()
# 리스트의 얕은 사본을 돌려준다. a[:]와 동등

copy_list = Venti_menu.copy()
print(id(Venti_menu), id(copy_list)) # 객체의 id 값이 다르다.


# < 리스트 컴프리헨션 >============================================================
# 리스트 컴프리헨션은 리스트를 만드는 간결한 방법을 제공
# =================================================================================

squares1 = list(map(lambda x: x**2, range(10)))
squares2 = [x**2 for x in range(10)]

combs1 = [(x, y) for x in [1,2,3] for y in [3,1,4]]
combs2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs2.append((x, y))
print(squares1)
print(squares2)
print(combs1)
print(combs2)

# del 문 =========================================================================================
# 리스트에서 값을 삭제할 때 remove(), pop() 메서드 뿐만 아니라 del 키워드로 삭제할 수 있다.

dessert = ['호두과자', '앙버터 치즈볼', '모짜 치즈볼', '미니붕어빵', '크로와상', '머핀', '슈스틱', '샌드위치']
print(id(dessert), id(dessert[:])) # id 값이 다르다
del dessert[-1] # 1개 삭제
print(dessert) # ['호두과자', '앙버터 치즈볼', '모짜 치즈볼', '미니붕어빵', '크로와상', '머핀', '슈스틱']
del dessert[-4:5] # 슬라이스로 부분삭제
print(dessert) # ['호두과자', '앙버터 치즈볼', '모짜 치즈볼', '머핀', '슈스틱']
del dessert[:] # 전체삭제
print(dessert) # []



# < 튜플 > =========================================================================================
# 튜플은 시퀀스 자료형이면서 "불변" 이고, 리스트는 "가변"이다.

t1 = () # 빈 튜플 만들기1
t2 = ('hello',) # 요소가 1개인 튜플
t3 = tuple() # 빈 튜플 만들기2
print(type(t1), type(t2), type(t3))




# < 집합 > =========================================================================================
# 집합(Set)은 순서가 없고 중복되는 요소가 없는 컬렉션이다. 중괄호 {} 로 표기한다. 
# 빈(Empty) 집합을 만들 때는  {}가 아니라 set() 을 사용해야 한다.
# {}를 사용하면 set이 아니라 빈 딕셔너리를 만든다

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana', 'kiwi', 'mango'}
print(basket) # {'mango', 'banana', 'pear', 'apple', 'orange', 'kiwi'}
print('melon' not in basket) # True
print('kiwi' in basket)      # True
a = set('fewqefdasqqrdafqweqefas')
b = set('zvczvvzbzxdsvzszsdfvczsadf')
print(a) # {'d', 'r', 'q', 'a', 'w', 's', 'e', 'f'}
print(b) # {'d', 'v', 'z', 'b', 'a', 'x', 's', 'c', 'f'}
print(a - b) # {'q', 'w', 'e', 'r'}
print(a | b) # {'c', 'q', 'w', 's', 'r', 'v', 'a', 'x', 'z', 'f', 'd', 'b', 'e'}
print(a & b) # {'d', 's', 'a', 'f'}
print(a ^ b) # {'c', 'q', 'v', 'r', 'w', 'x', 'z', 'b', 'e'} exclusive or(XOR)




# < 딕셔너리 > =========================================================================================
# 딕셔너리는 키(key)로 인덱싱하는데 키는 모든 불변형을 사용할 수 있다(문자열, 숫자들은 항상 키가 될 수 있다.)
# 튜플이 직접적이나 간접적으로 가변 객체를 포함한다면, 딕셔터리의 키로 사용될 수 없다.
# (튜플이 문자열, 숫자, 튜플들만 포함하면, 딕셔너리의 키로 사용할 수 있다.)
# 딕셔너리를 만들 때는 다음과 같이 만들 수 있다.

dict1 = { } # 빈(Empty) 딕셔너리 생성
dict2 = {'name': 'GwangHyeon', 'age':25, 'grade':{'math': 95, 'science': 85, 'english':93}} # key:value로 생성
dict3 = dict([('Olivia',22), ('Charlotte',23), ('Isabella', 21)]) # 생성자로 만들기1
dict4 = dict() # 생성자로 만들기2

print(dict1, dict2, dict3, dict4, sep=' AND ')


# 딕셔너리의 루프 테크닉
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(f'key = {k}, value = {v}')

# 시퀀스를 루핑할 때는 enumerate() 함수를 사용하면 인덱스와 값을 가져올 수 있다.
for i, v in enumerate(['DNS Server', 'router', 'ISP']):
    print(f'index = {i}, value = {v}')

# 2개 또는 그 이상의 시퀀스를 동시에 루핑하려면, zip() 함수를 사용
# zip() 함수는 시퀀스 중에서 가장 짧은 시퀀스에 맞춰 루핑한다.
icecream = ('블랙 할로윈', '우낀소(우유속에 끼인 소보로)', '파핑파핑 바나나', '너는 참 달고나', '에스프레소 앤 크림', '레인보우 샤베트')
coffee = ['바닐라빈 라떼', '에스프레소 아포가토', '연유 라떼', '카페 모카']
cake = ('빙그르르 마카롱', '치즈 고구마 케이크구마', '용감한 내 친구 카봇', '듀얼 와츄원 NO.9', '해피데이 카카오프렌즈')
for menu1, menu2, menu3 in zip(icecream, coffee, cake):
    print('나는 {0}랑 {1}랑 {2} 주세요'.format(menu1, menu2, menu3))


# < 조건 더 보기 > =========================================================================================
'''
1)  비교 연산자 in 과 not in은 값이 시퀀스에 있는지(없는지) 검사한다.
2)  연산자 is와 is not 은 두 객체자 진짜로 같은 객체인지 비교한다.
3)  모든 비교 연산자들은 같은 우선순위를 가지고, 모든 산술 연산자들보다 낮습니다.
4)  비교는 연쇄할 수 있습니다. 예를 들어, a < b == c는 a가 b보다 작고, 동시에 b가 c와 같은지 검사한다.
5)  비교는 논리 연산자 and 와 or 를 사용해서 결합할 수 있고, 비교의 결과는 (또는 그 밖의 모든 논리 표현식은) not 으로 부정될 수 있습니다.
    not이 가장 높은 우선순위를 갖고, or가 가장 낮습니다. 그래서 A and not B or C 는 (A and (not B)) or C 와 동등합니다.
'''

# 시퀀스의 비교 연산 =========================================================================================
sequence1 = [1, 2]
sequence2 = [1, 2]
print(sequence1 is sequence2) # False

print( (1, 2, 3) < (1, 2, 4) ) # True
print( [1, 2, 3] < [1, 2, 4] ) # True
print( 'ABC' < 'C' < 'Pascal' < 'Python' ) # True
print( (1,2,3,4) < (1,2,4) ) # True
print( ('AA', 'BB', 'CC') < ('AA', 'BB') ) # False
print( [1, 2, 3] == [1.0, 2.0, 3.0] ) # True
print( (1, 2, ('AA', 'AB')) < (1, 2, ('ABC', 'AB'), 4) ) # True




