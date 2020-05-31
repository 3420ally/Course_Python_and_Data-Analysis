print('1785103 이수연')

## 실습1
# 성별 연령별 인구 데이터 저장하기
import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
name = input("궁금한 동네를 입력해주세요: ")
for row in data: #데이터를 한 줄씩 읽어들임
    if name in row[0]:
        for i in range(3,104): #줄 안에서 남성/여성 데이터를 0~100세 이상 한줄한줄 읽어들임
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break #첫번째 줄만 읽어들이고 종료

# 성별 연령별 인구 데이터 꺾은선 그래프로 표현하기
import matplotlib.pyplot as plt
plt.plot(m,label='Male')
plt.plot(f,label='Female')
plt.legend()
plt.show()

## 실습2
# 연령별 (남성인구-여성인구) 값 그래프로 표현하기
import csv
f = open('gender.csv')
data = csv.reader(f)
result = []
name = input("궁금한 동네를 입력해주세요: ")
for row in data:
    if name in row[0]:
        for i in range(3,104):
            result.append(int(row[i]) - int(row[i+103])) #남성데이터-여성데이터
        break
import matplotlib.pyplot as plt
plt.bar(range(101),result) # x축: 0~100의 정수값 / y축: result
plt.show()

## 실습3
# 버블 차트로 표현하기
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.scatter([1,2,3,4],[10,30,20,40], s=[100,200,250,300])
plt.show()

# 버블 차트로 표현하기(컬러맵 추가)
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.scatter([1,2,3,4],[10,30,20,40], s=[30,60,90,120], c=range(4), cmap='jet')
#colorbar에 0~3의 값이 만들어진 후 각 값에 각각의의색깔 배정
plt.colorbar()
plt.show()

## 실습4
# 위치, 크기가 서로 다른 100개의 점 만들기
import matplotlib.pyplot as plt
import random #랜덤하게 값이 결정됨

x = []
y = []
size = []
for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50, 100))
    size.append(random.randint(10, 100))
plt.style.use('ggplot')
plt.scatter(x,y,s=size)
plt.show()

# 위치, 크기가 서로 다른 100개의 점 만들기(투명도 설정)
import matplotlib.pyplot as plt
import random #랜덤하게 값이 결정됨

x = []
y = []
size = []
for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50, 100))
    size.append(random.randint(10, 100))
plt.style.use('ggplot')
plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7)
# alpha: 투명도 설정, 1로 갈수록 불투명, 뒤에 가리는 점들을 파악하기에 유리
plt.colorbar()
plt.show()

# 추세선 그리기
import matplotlib.pyplot as plt
plt.plot(range(max([4,3,5,1])), range(max([4,3,5,1])),'g')
# range(max([4,3,5,1]) = range(5) = [0,1,2,3,4]
plt.show()
print(range(5)) #결과값 range(0,5)
print(list(range(5))) #결과값 [0,1,2,3,4]

## 실습5
# 연령대별 성별 비율 산점도로 표현하기 (원의 크기는 인구수의 제곱근)
import csv
import math
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
size = [] # 여성인구+남성인구 합한 값 -> 각 버블들의 크기 결정
name = input("궁금한 동네를 입력해주세요: ")
for row in data: #데이터를 한 줄씩 읽어들임
    if name in row[0]:
        for i in range(3,104): #줄 안에서 남성/여성 데이터를 0~100세 이상 한줄한줄 읽어들임
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(math.sqrt(int(row[i]) + int(row[i+103])))
            # 여성인구 + 남성인구의 sqrt 값을 size에 집어넣음
        break #첫번째 줄만 읽어들이고 종료

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(10,5), dpi=300) #그래프의 크기 지정
plt.title( name + '지역의 성별 인구 그래프')
plt.scatter(m, f, s=size, c=range(101), cmap='jet', alpha=0.5)
plt.colorbar()
plt.plot(range(max(m)), range(max(m)),'g')
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
plt.show()

