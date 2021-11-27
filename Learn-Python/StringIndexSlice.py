stmt = 'Coffee is a brewed drink prepared from roasted coffee beans'
stmtkr = "영어권에서는 더치커피라는 단어 자체가 없으며, 찬물을 통해 낸 커피를 모두 '콜드브루' 라고 통칭"


print(len(stmt))        # 59
print(stmt[10:40])      # a brewed drink prepared from r
print(stmt[10:30:2])    # abee rn rp
print(stmt[-50:-30:2])  # '  rwddikpe'
print(stmt[-50], stmt[-30]) # stmt[-50] = ' '(공백) , stmt[-30] = 'a'

print(len(stmtkr[-20:-40:2])) # 0
# 슬라이싱 [start:stop:step]에서 stop이 start보다 작고 step이 양수이면, 결과는 ''(길이가 0인 문자열)
# 마찬가지로 stop이 start보다 크고 step이 음수이면, 결과는 똑같다.

print(stmtkr[-10:-30:-2]) # 드'두 피  통을찬
print(stmt[::]== stmt[:]) # start, stop, step은 기본값이 있다.(start: 0, stop: 매개변수값, step:1)
print(stmt[:1000])        # stop값이 인덱스 범위를 초과해도 된다

print(stmt[:10]+stmt[10:20]+stmt[20:100])
print(stmtkr[::-2])       # 칭 라'브콜 모를커낸해 물 며없가자어 라커더는에어






