from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

wd=webdriver.Chrome("C:/chromedriver/chromedriver.exe")
wd.get('https://www.airport.kr/ap/ko/dep/depPasSchList.do')
wd.set_window_size(1200,900)

time.sleep(3)

searchBox=wd.find_elements_by_css_selector('select[class="search-flight-detail-select-article"]')

searchBox[1].click()

#날짜 지정
searchBox[1].find_element_by_css_selector("option[value='20191212']").click()
time.sleep(1)

#시간 지정(시작 시간, 종료시간) 00시00분 ~ 23시59분 까지
start_end_time=wd.find_element_by_css_selector('div[class="search-flight-detail-select-article double"]')

#시작 시간을 00시 00분으로 맞춤
start_end_time.find_element_by_css_selector('#FROM_TIME > option[value="0000"]').click()
time.sleep(1)
#종료 시간을 23시 59분으로 맞춤
start_end_time.find_element_by_css_selector('#TO_TIME > option[value="2359"]').click()
time.sleep(1)

wd.find_element_by_css_selector('#searchform button[id="searchBtn"][class="search-flight-detail-select-btn ico"]').click()
time.sleep(7)


soup=BeautifulSoup(wd.page_source, 'html.parser') #html 파싱



print(soup.title.getText().replace('\t','').replace('\n','')) #getText(), text, get_text(), string
#soup.findAll('a'), soup.find_all('a'), soup.select('a')
table=soup.select('#div-result-list > div[class="table-like vt-dark"]') #전체를 감싸고 있는 가장 바깥쪽 div태그
print('completed')

#class속성이 codeshare-wrap 또는 flight-wrap인 엘리먼트를 리스트로 가져온다
result=table[0].select('div[class="codeshare-wrap"], div[class="flight-wrap"]')

#print(len(result))
#print(result[0].select('a > div')[0].getText().replace('\n','').replace('\t',''))
#print(result[0].select('a > div')[1].getText().replace('\n','').replace('\t',''))

time.sleep(1)

"""
for a in result:
    subList1=a.select('a > div')
    for b in subList1:
        print(b.getText().replace('\n', '').replace('\t', ''))

"""


"""
for a in result:
    subList1=a.select('a > div')
    for b in subList1:
        subList2=b.select('div[class^="td-like"]')
        for c in subList2:
            print(c.getText().replace('\n','').replace('\t',''), end=" ")
        print('')
"""
total=[]

for a in result:
    subList1=a.select('a > div')
    for b in subList1:
        subList2=b.select('div[class^="td-like"]')
        lineTemp=[]
        for c in subList2:
            lineTemp.append(c.getText().replace('\n','').replace('\t',''))
        total.append(lineTemp)

print('crawling completed!!')

#00:0300:05를 00시03분 으로 바꾼다
for s in range(len(total)):
	total[s][0]=total[s][0][0:5].replace(':','시')+'분'

df=pd.DataFrame(total, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
df.to_csv('1212Departure.csv', encoding='euc-kr')#1203 날짜


wd.quit()
