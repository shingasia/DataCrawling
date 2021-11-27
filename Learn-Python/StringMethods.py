names = 'olivia, emma, ava, charlotte, sphia, isabella, abigail, evelyn'
similarwords ="AcceptExcept AdviceAdvise AffectEffect AmongBetween AssureEnsureInsure ImplyInfer"

#=========================== 1. capitalize()
print(names.capitalize()) 
# 첫 문자가 대문자이고 나머지가 소문자인 문자열의 복사본을 돌려줍니다.

#=========================== 2. center(width[, fillchar])
print('Olivia'.center(30, 'Z'))
# 길이 width 인 문자열의 가운데에 정렬한 값을 돌려줍니다. 지정된 fillchar (기본값은 ASCII 스페이스)을 사용하여 채웁니다. width 가 len(s) 보다 작거나 같은 경우 원래 문자열이 반환됩니다.
# ZZZZZZZZZZZZOliviaZZZZZZZZZZZZ

#=========================== 3. count(sub[, start[, end]])
print(similarwords.count('ss'))
# 범위 [start, end] 에서 부분 문자열 sub 가 중첩되지 않고 등장하는 횟수를 돌려줍니다.

#=========================== 4. encode(encoding="utf-8", errors="strict")
print(similarwords.encode('utf-16', errors='strict'))
# 문자열의 바이트열 객체로 인코딩된 버전을 돌려줍니다. 기본 인코딩은 'utf-8' 입니다. errors 는 다른 오류 처리 방식을 설정하기 위해 제공될 수 있습니다.


#=========================== 5. endswith(suffix[, start[, end]])
print(names.endswith(', evelyn'))                           # True
print(names.endswith(('lyn', 'evelyn', 'l, evelyn', None))) # True
print(names.endswith(('AAA', 'BBB', 'CCC')))                # False
# 문자열이 지정된 suffix 로 끝나면 True 를 돌려주고, 그렇지 않으면 False 를 돌려줍니다. 
# suffix 는 찾고자 하는 접미사들의 튜플이 될 수도 있습니다.


#=========================== 6. find(sub[, start[, end]]), rfind(sub[, start[, end]])
print('SSAAASSSSSSAAAASSSSSSAAAAASASASAAAAAASSSSSSSAA'.find('AAAA'))  # 11
print('SSAAASSSSSSAAAASSSSSSAAAAASASASAAAAAASSSSSSSAA'.rfind('AAAA')) # 33
# find = 부분 문자열 sub 가 슬라이스 s[start:end] 내에 등장하는 가장 작은 문자열의 인덱스를 돌려줍니다. 없으면 -1을 돌려줍니다.
# rfind = 부분 문자열 sub 가 s[start:end] 내에 등장하는 가장 큰 문자열의 인덱스를 돌려줍니다. 없으면 -1을 돌려줍니다.

#=========================== 7. format(*args, **kwargs)
print('My name is {} my age is {} and I\'m very happy to meet {}'.format('Sena', 22, 'Henry'))
print('{0} 더하기 {1} 은 {2}입니다. 정답{2}'.format(10, 20, 10+20))
print('나는 {0}년 부터 {1}년 까지 {2}에서 일을했어요. {0}년 보다 {1}에 일을 더 오래했어요.'.format(2019, 2020, '서울'))
print('여행가서 {area1}에서는 {dish1}과 {dish2}을(를) 먹었고 돌아오면서 {area2}에 들려 {dish3}도 먹었다.'.format(area1='오사카', area2='교토', dish1='문어빵', dish2='이치란라멘', dish3='복숭아콜라'))
Lotion = {'color':'purple', 'size':'500ML', 'price':12900, 'name':'존슨즈베이비 베드타임 바디로션', '바코드':8801008101247}
print('색상 = {color}, 크기 = {size}, 가격 = {price}, 이름 = {name}, 바코드 = {바코드}'.format(**Lotion))
Goods = [
    {'category':'도서', 'name':'데이터베이스론', 'price':21000},
    {'category':'청소용품', 'name':'물걸레청소포', 'price':2000},
    {'category':'식품', 'name':'화이트쿠키 빼빼로', 'price':1300},
    {'category':'가구', 'name':'침대(슈퍼싱글)', 'price':290000}
]
class MyRoom:
    def __init__(self):
        self.size=20.5
        self.floor=9
        self.books=[{'name':'BasicEnglish', 'page':500, 'series':[1,2,3]},
                    {'name':'BasicPython', 'page':700, 'series':[3.5, 3.6, 3.7]}]
        pass
    pass


print('카테고리 = {0[category]}, 이름 = {0[name]}, 가격 = {0[price]}'.format(*Goods))
print('카테고리 = {p[1][category]}, 이름 = {p[1][name]}, 가격 = {p[1][price]}'.format(p=Goods))
print('{.size}'.format(MyRoom())) # 20.5
print('(넓이, 층) = ({obj.size}, {obj.floor}), \
    책1 = {obj.books[0][name]} {obj.books[0][page]} {obj.books[0][series]} \
    책2 = {obj.books[1][name]} {obj.books[1][page]} {obj.books[1][series]}'.format(obj=MyRoom()))
# (넓이, 층) = (20.5, 9),     책1 = BasicEnglish 500 [1, 2, 3]     책2 = BasicPython 700 [3.5, 3.6, 3.7]

#=========================== 8. index(sub[, start[, end]]), rindex(sub[, start[, end]])
print('index() method')
print('EEEEMMEEEEMMMMMEEEMEEEEEEEMMMMEEEE'.index('EEE'))  # 0
print('EEEEMMEEEEMMMMMEEEMEEEEEEEMMMMEEEE'.rindex('EEE')) # 31
# find() 과 비슷하지만, 부분 문자열을 찾을 수 없는 경우 ValueError 를 일으킵니다.

# ▶▶▶▶▶ 쉽게 생각해 index, find는 왼쪽부터 찾고, rindex, rfind는 오른쪽부터 찾는다.



#=========================== 9. isalnum()
# 문자열 내의 모든 문자가 알파벳과 숫자이면 True 그렇지 않으면 False를 리턴
#=========================== 10. isalpha()
# 문자열 내의 모든 문자가 알파벳이면 True 그렇지 않으면 False를 리턴
#=========================== 11. isascii()
# 문자열이 비어 있거나 문자열의 모든 문자가 ASCII이면 True 그렇지 않으면 False를 리턴
#=========================== 12. isdecimal()
# 문자열 내의 모든 문자가 십진수 문자이면 True 그렇지 않으면 False를 리턴
#=========================== 13. isdigit()
# 문자열 내의 모든 문자가 디짓이면 True 그렇지 않으면 False를 리턴
#=========================== 14. islower()
# 문자열 내의 모든 케이스 문자가 소문자이고, 적어도 하나의 케이스 문자가 존재하면 True
#=========================== 15. isnumeric()
# 문자열 내의 모든 문자가 숫자이면 True
#=========================== 16. isspace()
# 문자열이 공백 문자만 있으면 True
#=========================== 17. isupper()
# 문자열 내의 모든 케이스 문자가 대문자이고, 적어도 하나의 케이스 문자가 존재하면 True
#=========================== 18. join(iterable)
print(' ABCDE '.join(['INT1', 'INT2', 'INT3', 'INT4', 'INT8'])) # INT1 ABCDE INT2 ABCDE INT3 ABCDE INT4 ABCDE INT8
#=========================== 19. ljust(width[, fillchar])
print('Seraphic'.ljust(30, '='))
# 왼쪽으로 정렬된 문자열을 길이 width 인 문자열로 돌려줍니다. 지정된 fillchar (기본값은 ASCII 스페이스)을 사용하여 채웁니다.
#=========================== 20. rjust(width[, fillchar])
print('Blossom'.rjust(30, '='))
# 오른쪽으로 정렬된 문자열을 길이 width 인 문자열로 돌려줍니다. 지정된 fillchar (기본값은 ASCII 스페이스)을 사용하여 채웁니다.
#=========================== 21. lower()
print('MoOnLiGhT 는 달빛이다.'.lower())
# 모든 케이스 문자 4 가 소문자로 변환된 문자열의 복사본을 돌려줍니다.
#=========================== 22. upper()
print('CreSeNt는 초승달 이라는 뜻이다.'.upper())
# 모든 케이스 문자 4 가 대문자로 변환된 문자열의 복사본을 돌려줍니다
#=========================== 23. lstrip([chars]), rstrip([chars]), strip([chars])
print('equivalentcertificate'.lstrip('etquic')) # valentcertificate
print('equivalentcertificate'.rstrip('etquic')) # equivalentcertifica
print('equivalentcertificate'.strip('etquic'))  # valentcertifica
# 각각 선행(lstrip)/후행(rstrip)/선행과 후행 모두(strip) 문자가 제거된 문자열의 복사본을 돌려줍니다. chars 인자는 제거할 문자 집합을 지정하는 문자열입니다. 
# 생략되거나 None 이라면, chars 인자의 기본값은 공백을 제거

#=========================== 24. replace(old, new[, count])
print('Lovesome, Sonorout, Serendipity, Eloquence'.replace(', ', 'PYTHON'))
# 모든 부분 문자열 old 가 new 로 치환된 문자열의 복사본을 돌려줍니다. 선택적 인자 count 가 주어지면, 앞의 count 개만 치환





