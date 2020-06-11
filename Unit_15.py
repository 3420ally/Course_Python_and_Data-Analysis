print('1785103 이수연')

## 위키피디아 데이터 엑셀로 저장하기
import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
#print(df) #테이블 형태
print("type(df)")
print(type(df)) #<class 'list'>

print("df[1] Start")
print(df[1]) #1번 인덱스에 저장된 내용 출력
print("df[0] Start")
print(df[0]) 

import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
#해당 사이트 url주소 입력, header=첫번째행(없으면 None), 행의 index=첫번째열
print(df[1])

summer = df[1].iloc[0:,:5] #행 전체, 5번째 열까지 저장
#print(summer)

summer.columns=['경기수','금','은','동','계']
print(summer)
print(summer.sort_values('금', ascending=False)) #금메달 내림차순으로 정렬

#엑셀파일로 저장
summer.to_excel('하계올림픽메달.xlsx') #정리된 파일을 xlsx로 저장


## 데이터 프레임 기초
import pandas as pd
index = pd.date_range('1/1/2000', periods=8) #2000년 1월 1일부터 8개의 index 만듦
print(index)

import numpy as np
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df) #8행 3열 데이터프레임. 컬럼명 A B C, 인덱스 위에서 만들어진 날짜 인덱스, 각 원소 random 실수

print("B열")
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df['B']) #B열만 뽑아내기 -> Series(1차원) 형태

print(df['B']>0.4) #컬럼 B의 값이 0.4 보다 크면 True, 작으면 False 출력

df2 = df[df['B']>0.4]
print(df2) #조건을 만족하는 행만 가져오기(A,C값들도 포함)

df2 = df2.T
print(df2) #행과 열 transpose


# 데이터프레임의 행 우선 계산과 열 우선 계산
import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D']=df['A']/df['B'] #A열값/B열값을 D열에 저장
print('A열의 값을 B열의 값으로 나눈 값을 D열에 저장')
print(df)

df['E']=np.sum(df, axis=1) #열 우선 계산값을 E열에 저장 #A열~D열 더한 값을 E열에 저장
print("열 우선 계산값 _ A~D열 합 E열에 저장")
print(df.head()) #5행까지 출력

df = df.sub(df['A'],axis=0) #A열의 데이터를 기준으로 행 우선 계산
print("A열의 데이터를 기준으로 행 우선 계산_각 열에서 A열 뺀 값")
print(df.head()) #각 열의 값-같은 행에 있는 A열 값

df = df.div(df['C'],axis=0) #C열의 데이터를 기준으로 행 우선 계산
print("C열의 데이터를 기준으로 열 우선 계산_각 열 데이터를 C열로 나눈 값")
print(df.head()) #각 열의 값/C열의 값

df.to_csv('test.csv')


## Pandas로 인구 구조 분석하기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
df = pd.read_csv('age_v2.csv', encoding='cp949', index_col=0) #첫번째 column을 index로

df = df.div(df['총인구수'], axis=0) #전체 데이터를 총인구수로 나눠서 비율로 변환, 컬럼 방향
del df['총인구수'], df['연령구간인구수'] #총인구수, 연령구간인구수 열 삭제

name = input('원하는 지역의 이름을 입력해주세요: ') #지역 이름 입력
a = df.index.str.contains(name) #name에 해당하는 행을 찾아서 해당 지역의 인구 구조를 저장
df2 = df[a] #그 중 a에 있는 값만 가져옴

df.loc[np.power(df.sub(df2.iloc[0], axis=1),2).
           sum(axis=1).sort_values().index[:5]].T.plot()


import numpy as np
x = df.sub(df2.iloc[0], axis=1) #궁금한 지역 A의 인구비율 - B의 인구 비율
y = np.power(x,2)
z = y.sum(axis=1)
i = z.sort_values().index[:5] #차이가 가장 작은 지역 top5 구하기 (index=지명) 저장
df.loc[i].T.plot() #index 기준으로 데이터 가져와서 결과를 꺾은선그래프로 표현
plt.show()





