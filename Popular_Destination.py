import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import time


#1203 부터 1212까지
df1203=pd.read_csv('1203Departure.csv', encoding='euc-kr')
df1204=pd.read_csv('1204Departure.csv', encoding='euc-kr')
df1205=pd.read_csv('1205Departure.csv', encoding='euc-kr')
df1206=pd.read_csv('1206Departure.csv', encoding='euc-kr')
df1207=pd.read_csv('1207Departure.csv', encoding='euc-kr')
df1208=pd.read_csv('1208Departure.csv', encoding='euc-kr')
df1209=pd.read_csv('1209Departure.csv', encoding='euc-kr')
df1210=pd.read_csv('1210Departure.csv', encoding='euc-kr')
df1211=pd.read_csv('1211Departure.csv', encoding='euc-kr')
df1212=pd.read_csv('1212Departure.csv', encoding='euc-kr')

time.sleep(1)

#데이터 프레임 전체를 리스트에 저장
df_list=[df1203, df1204, df1205, df1206, df1207, df1208, df1209, df1210, df1211, df1212]

# Unnamed:0 칼럼을 제거한다
# df1203.drop(df1203.columns[[0]], axis=1, inplace=True)
for dfTemp in df_list:
    dfTemp.drop(dfTemp.columns[[0]], axis=1, inplace=True)

#데이터 프레임 10개를 전부다 total_df 로 합친다
total_df=pd.concat(df_list, ignore_index=True)


destinations=dict()     #(목적지: 운항횟수)를 쌍으로 저장할 딕셔너리 생성


for des in list(total_df['목적지']):
    if des not in destinations :
        destinations[des]=1#없으면 추가
    else:
        destinations[des]=destinations[des]+1#있으면 1씩 증가



df=pd.DataFrame({'Destination' : list(destinations.keys()), 'frequency': list(destinations.values())})

#저장 !!!!!!!!!!!!!!!!!!!!!!!
#df.to_csv('Flying_Frequency.csv', encoding='euc-kr')

x=list(destinations.values())
y=list(destinations.keys())
plt.barh(y, x)
plt.show()

