import pandas as pd
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
time1=[]    #0000~0259
time2=[]    #0300~0559
time3=[]    #0600~0859
time4=[]    #0900~1159
time5=[]    #1200~1459
time6=[]    #1500~1759
time7=[]    #1800~2059
time8=[]    #2100~2359

#3시간 단위로 나눠서 시간대별 운항편
for a in range(len(total_df)):
    temp=total_df.loc[a, '출발시간'].replace('시','').replace('분','')
    if temp < '0300' :
        time1.append(list(total_df.loc[a]))
    elif temp < '0600' :
        time2.append(list(total_df.loc[a]))
    elif temp < '0900' :
        time3.append(list(total_df.loc[a]))
    elif temp < '1200' :
        time4.append(list(total_df.loc[a]))
    elif temp < '1500' :
        time5.append(list(total_df.loc[a]))
    elif temp < '1800' :
        time6.append(list(total_df.loc[a]))
    elif temp < '2100' :
        time7.append(list(total_df.loc[a]))
    else:
        time8.append(list(total_df.loc[a]))

print('completed')

time_df1=pd.DataFrame(time1, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
time_df2=pd.DataFrame(time2, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
time_df3=pd.DataFrame(time3, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
time_df4=pd.DataFrame(time4, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
time_df5=pd.DataFrame(time5, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
time_df6=pd.DataFrame(time6, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
time_df7=pd.DataFrame(time7, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])
time_df8=pd.DataFrame(time8, columns=['출발시간', '목적지', '운항편/항공사', '터미널', '체크인 카운터', '탑승구', '출발현황', '운항속보'])


#저장
time_df1.to_csv('time1.csv', encoding='euc-kr')
time_df2.to_csv('time2.csv', encoding='euc-kr')
time_df3.to_csv('time3.csv', encoding='euc-kr')
time_df4.to_csv('time4.csv', encoding='euc-kr')
time_df5.to_csv('time5.csv', encoding='euc-kr')
time_df6.to_csv('time6.csv', encoding='euc-kr')
time_df7.to_csv('time7.csv', encoding='euc-kr')
time_df8.to_csv('time8.csv', encoding='euc-kr')

print('saved')

