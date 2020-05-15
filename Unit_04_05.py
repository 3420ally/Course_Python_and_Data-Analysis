print("1785103 이수연")

# matplotlib 라이브러리의 pyplot 모듈을 'plt'라는 별명으로 부르기(as,alias)
import matplotlib.pyplot as plt

## 기본 그래프 그리기
plt.plot([10,20,30,40])
plt.show() #결과값 일차직선. y값은 입력값, x값은 0부터 1씩 증가(디폴트)

plt.plot([1,2,3,4], [12,43,25,15]) #입력값을 각각 x, y값에 대응
plt.show()

## 그래프에 옵션 추가하기

# 그래프에 제목 넣기
plt.title('plotting')
plt.plot([10,20,30,40])
plt.show()

# 그래프에 범례 넣기
plt.title('legend')
plt.plot([10,20,30,40], label = 'asc') #증가를 의미하는 asc 범례
plt.plot([40,30,20,10], label = 'desc') #감소를 의미하는 desc 범례
plt.legend() #범례 실행시키기 위해서는 꼭 넣어야함
plt.show()

# 그래프 색상 바꾸기
plt.title('color') #제목 설정
plt.plot([10,20,30,40], color = 'skyblue', label = 'skyblue') #하늘색 그래프
plt.plot([40,30,20,10], 'pink',label = 'pink') #분홍색 그래프, 'color= ' 생략가능
plt.legend() #범례 표시
plt.show()

# 그래프 선 모양 바꾸기
plt.title('linestyle') #제목 설정
plt.plot([10,20,30,40], color = 'r', linestyle = '--', label = 'dashed') #빨간색 dashed선 그래프
plt.plot([40,30,20,10], color = 'g', ls = ':', label = 'dotted') #초록색 dotted선 그래프
plt.legend() #범례 표시
plt.show()

plt.title('marker') #마커 그래프= 산점도
plt.plot([10,20,30,40],'r.', label = 'circle') #빨간색 원형(색깔+'.' 형태) 마커 그래프
plt.plot([40,30,20,10],'g^', label = 'triangle up') #초록색 삼각형(색깔+'^'형태) 마커 그래프
plt.legend() #범례 표시
plt.show()


## 내 생일의 기온 변화를 그래프로 나타내기

# 최고 기온 데이터를 꺾은선 그래프로 그리기
import csv
import matplotlib.pyplot as plt
f = open('seoul.csv') #데이터 읽어들이기
data = csv.reader(f) #데이터 읽기
next(data) #header부분 삭제
result = [] #빈 리스트 만들어 최고기온 담기

for row in data:
    if row[-1] != '': #문자열이 아닌 경우 오류 발생 -> 문자열 아닌 경우 result 리스트에 담기
        result.append(float(row[-1])) #숫자로 변환해 담기

plt.plot(result, 'r') #result 리스트에 저장된 값을 빨간색 그래프로 그리기
plt.show() #그래프 나타내기


# 날짜 데이터 추출하기
date = '1907-10-01'
print(date.split('-')) #'-'를 기준으로 세 결과로 나누어서 리스트로 반환

print(date.split('-')[0])
print(date.split('-')[1])
print(date.split('-')[2])

# 8월의 최고기온 데이터 시각화하기
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            result.append(float(row[-1]))

import matplotlib.pyplot as plt
#plt.figure(dpi=300)
plt.plot(result,'hotpink')
plt.show()

# 내 생일의 최고 기온 데이터 시각화하기
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08' and row[0].split('-')[2] == '12': #월, 일 값 고정
            result.append(float(row[-1]))

import matplotlib.pyplot as plt
#plt.figure(dpi=300)
plt.plot(result,'hotpink')
plt.show()

# 내 생일의 최고기온 및 최저기온 데이터 시각화하기
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = [] #최고기온값을 high 리스트에 저장
low = [] #최저기온값을 low 리스트에 저장

for row in data:
    if row[-1] != '' and row[-2] != '': #최고와 최저 둘다 누락되지 않는 것 중
        if row[0].split('-')[1] == '08' and row[0].split('-')[2] == '12': #월, 일 값 고정
            high.append(float(row[-1])) #최고기온 high에 저장
            low.append(float(row[-2])) #최저기온 low에 저장

import matplotlib.pyplot as plt
#plt.figure(dpi=300)
plt.plot(high,'hotpink') #최고기온은 핫핑크로
plt.plot(low, 'skyblue') #최저기온은 하늘색으로
plt.show()


## 내 생일의 최고 기온 및 최저 기온 데이터 시각화하기 최종 완성
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = [] #최고기온값을 high 리스트에 저장
low = [] #최저기온값을 low 리스트에 저장

for row in data:
    if row[-1] != '' and row[-2] != '': #최고와 최저 둘다 존재한다면
        date = row[0].split('-') #날짜 값을 '-'를 기준으로 구분하여 저장

        if 1998 <= int(date[0]): #1998년 이후 데이터라면

            if date[1]=='08' and date[2]=='12': #8월 12일이라면
                high.append(float(row[-1])) #최고기온 high에 저장
                low.append(float(row[-2])) #최저기온 low에 저장

                plt.rc('font', family = 'Malgun Gothic') #맑은 고딕을 기본 글꼴로 설정
plt.rcParams['axes.unicode_minus'] = False #마이너스 기호 깨짐 방지

plt.title('이수연 역대 생일의 기온 변화 그래프') #제목 생성
plt.plot(high, 'hotpink', label = 'high') #high 리스트에 저장된 값을 hotpink색으로 + 레이블 표시
plt.plot(low, 'skyblue', label = 'low') #low 리스트에 저장된 값을 skyblue색으로 + 레이블 표시
plt.legend() #범례 표시
plt.show() #그래프 나타내기