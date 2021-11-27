orderSequence = [
    {'size' : '파인트', 'icecream': ['치즈 고구마구마', '블래 할로윈', '찰떡콩떡',], 'price': 8200},
    {'size' : '쿼터', "icecream" : ['허쉬 쿠키&모찌', '체다치즈 앤 포테이토', '우유속에 끼인 소보로', '오레오 쿠키 앤 크림',], 'price': 15500},
    {'size' : '패밀리', 'icecream': ['월넛', '파핑파핑 바나나', '에스프레소 앤 크림', '엄마는 외계인', '너는 참 달고나'], 'price': 22000},
    {'size': '하프갤런', 'icecream': ['사랑에 빠진 딸기', '뉴욕 치즈케이크', '베리베리 스트로베리', '레인보우 샤베트', '이상한 나라의 솜사탕', '바람과 함께 사라지다',], 'price': 26500}
]



def addMenu(*icecreams):
    sizeKV = {'파인트':8200, '쿼터': 15500, '패밀리': 22000, '하프갤런': 26500}

    for i in icecreams:
        if len(icecreams) == 3:
            size = '파인트'
            break
        elif len(icecreams) == 4:
            size = '쿼터'
            break
        elif len(icecreams) == 5:
            size = '패밀리'
            break
        elif len(icecreams) == 6:
            size = '하프갤런'
            break
        else:
            pass
        pass
    
    a = {'size': size, "icecream": list(icecreams), 'price': sizeKV[size]}
    orderSequence.append(a)
    print(F'{len(orderSequence)} 번째 메뉴가 추가되었습니다.')
    return a

addMenu('체리쥬빌레', '바닐라', '초콜릿 무스', '그린티', '마법사의 할로윈') # 메뉴추가

def printOrderList():
    for order in range(0, len(orderSequence)):
        print(F'{order+1} 번째 주문은 {orderSequence[order]["icecream"]} 이고 가격은 {orderSequence[order]["price"]}')
    


