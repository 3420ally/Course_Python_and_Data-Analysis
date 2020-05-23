print("1785103 이수연")

## 8장. 인구 구조를 다양한 형태로 시각화하기
# 막대그래프 그리기 - bar()함수
import matplotlib.pyplot as plt
plt.bar([0,1,2,4,6,10], [1,2,3,5,6,7])
plt.show()

# 막대그래프를 활용해 우리동네 인구구조 시각화하기
import csv
f = open('age.csv')
data = csv.reader(f)
result = []

for row in data:
    if "신도림" in row[0]:
        for i in row[3:]:
            result.append(int(i))

import matplotlib.pyplot as plt
plt.bar(range(101), result) #0세~100세 이상
plt.show()

# 수평막대그래프(barh()함수)를 활용해 우리동네 인구구조 시각화하기
# 항아리 모양 그래프 그리기

import csv  #성별 데이터 저장
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

name = input('찾고싶은 지역의 이름을 알려주세요: ')
for row in data:
    if name in row[0]:
        for i in row[3:104]: #남성데이터
            m.append(-int(i)) #차트에서 왼쪽으로 넘기기위해 음수화
        for i in row[106:]: #여성데이터
            f.append(int(i))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False #마이너스값 깨지지 않게
plt.title(name+"지역의 남녀 성별 인구 분포")
plt.barh(range(101), m, label='남성') #수평 bar graph
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()

## 9장. 우리동네 인구구조를 파이차트로 나타내기
# 파이차트 그리기 - pie() 함수
import matplotlib.pyplot as plt
plt.pie([10,20])
plt.show()

import matplotlib.pyplot as plt
size = [2441, 2312, 1031, 1233]
plt.axis('equal') #동그란 파이차트
plt.pie(size)
plt.show()

# 색 및 돌출 효과 지정
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic') #한글 깨지지 않도록
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', explode=(0,0,0.1,0), colors=color)
#autopct = autopercent, 비율 자동으로 표시 / explode = 특수한 구간이 두드러져보이게
plt.legend() #범례 표현
plt.show()

# 파이차트 이용하여 성별, 연령별 인구 데이터 출력하기
import csv
f = open('gender.csv')
data = csv.reader(f)
size = []

name = input('찾고싶은 지역의 이름을 알려주세요: ')
for row in data:
    if name in row[0]:
        m = 0 #남성 총합 저장할 변수
        f = 0
        for i in range(101): 
           m += int(row[i+3])
           f += int(row[i+106])
        break  #찾고자하는 지역 데이터만 읽어들이고 break
size.append(m) #남성데이터 다 합치기
size.append(f)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic') #한글 깨지지 않도록
color = ['crimson', 'darkcyan'] #남성데이터/여성데이터
plt.axis('equal')
plt.pie(size, labels=['남','여'], autopct='%.1f%%', colors=color, startangle=90)
#startangle = 디폴트는 3시방향 시작이지만 6시방향 시작으로 변경
plt.title(name+'지역의 남녀 성별 비율')
plt.show()
