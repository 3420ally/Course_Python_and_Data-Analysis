print("1785103 이수연")

#히스토그램(Histogram)
## 서울의 최고기온 그래프
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []  #누락값 없앤 결과를 result 리스트에 넣기

for row in data:  #누락된 데이터 없애기
    if row[-1] !=  '':
        result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.figure(figsize = (10,2), dpi = 300)
plt.plot(result,'r')
plt.show()

## Hist 함수
import matplotlib.pyplot as plt
plt.figure (dpi=300)
plt.hist([1,1,2,3,4,5,6,6,7,8,10]) #빈도수를 히스토그램으로
plt.show()

## 주사위 시뮬레이션
# n번 실행
import random
dice = []

n = int(input("시행 횟수:"))
for i in range(n): #반복 n번
    dice.append(random.randint(1,6)) #결과를 dice에 저장
print(dice)

import matplotlib.pyplot as plt
plt.figure(dpi=300)
plt.hist(dice,bins=6) #여섯 구간으로 나눔
plt.show()

## 8월의 최고기온 데이터 히스토그램으로 나타내기
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []

for row in data:
    month = row[0].split('-')[1]  #행의 첫번째 원소를 slice
    if row[-1] !=  '':  #누락 없애기
        if month == '08':
            aug.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.hist(aug, bins=100, color='r')
plt.show()

## 1월과 8월의 최고기온 데이터 히스토그램으로 나타내기
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data:
    month = row[0].split('-')[1]  #행의 첫번째 원소를 slice
    if row[-1] !=  '':  #누락 없애기
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.hist(aug, bins=100, color='r', label='Aug')
plt.hist(jan, bins=100, color='b', label='Jan')
plt.legend()
plt.show()

#상자그림(Boxplot)
## 최댓값, 최솟값, 3/4, 2/4, 1/4 값을 표현할 수 있는 상자그림
import matplotlib.pyplot as plt
plt.figure(dpi=300)
import random
result = []
for i in range(13): #13번 반복하여 result에 넣음
    result.append(random.randint(1,1000))
print(sorted(result))

import numpy as np
result = np.array(result) #데이터를 array로 변환
print("1/4: " + str(np.percentile(result.25))) #Q1 값 반환
print("2/4: " + str(np.percentile(result.50))) #Q2 값 반환
print("3/4: " + str(np.percentile(result.75))) #Q3 값 반환
plt.boxplot(result)
plt.show()

## 1월과 8월의 최고기온 데이터 상자 그림으로 표현하기
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data:
    month = row[0].split('-')[1]  #행의 첫번째 원소를 slice
    if row[-1] !=  '':  #누락 없애기
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.figure(dpi = 300)
# 각각 위아래로 표현
plt.boxplot(aug)
plt.boxplot(jan)
# 순서대로 하나의 그래프에 표현
plt.boxplot([aug,jan])
plt.show()

## 1월부터 12월의 최고기온 데이터 상자 그림으로 표현하기
import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
month = [[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data:
    if row[-1] != '':
        month [int(row[0].split('-')[1]) -1].append(float(row[-1]))  #index가 0부터 시작하므로 -1
plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(month)
plt.show()

## 8월 1일부터 31일까지 최고기온 데이터 상자 그림으로 표현하기
import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = [] #일별 데이터를 저장할 리스트
for i in range(31):
    day.append([]) #day 리스트 내 31개 리스트 생성
# day = [[]x31개]와 같음

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08': #8월이라면
            #최고기온값 저장
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
plt.style.use('ggplot') #그래프 스타일 지정
plt.figure(figsize=(10,5), dpi=300) #그래프 크기 수정
plt.boxplot(day,showfliers=False) #아웃라이어 값 생략
plt.show()

## 우리 동네 인구구조 시각화하기
import csv
f = open('age.csv')
data = csv.reader(f)

for row in data:
    print(row)

# 우리 동네 연령별 인구수 출력하기
import csv
f = open('age.csv')
data = csv.reader(f)

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            print(i)

# 우리 동네 연령별 인구수 result 리스트에 저장하기
import csv
f = open('age.csv')
data = csv.reader(f)
result = []

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            result.append(int(i))
print(result)

# 우리 동네 연령별 인구수 데이터 시각화하기
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.plot(result)
plt.show()

# 동네 이름 입력받기
import csv
f = open('age.csv')
data = csv.reader(f)
result = []
name = input("동네이름 입력:")

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            result.append(int(i))
print(result)

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.plot(result)
plt.show()