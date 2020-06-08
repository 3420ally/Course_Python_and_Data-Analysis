print("1785103 이수연")
## Numpy를 활용한 나만의 프로젝트 만들기 - age_v2.csv 사용
# 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기
import numpy as np
import csv

# 1. 데이터를 읽어온다.
f = open('age_v2.csv')
data = csv.reader(f)
next(data) #header부분 건너뛰기
data = list(data)

# 2. 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요: ')
mn = 1 #최솟값을 찾으려면 최대한 큰 값을 넣고, 최댓값을 찾으려면 최대한 작은 값 배정
result_name = ''
result = 0

# 3. 궁금한 지역의 인구 구조를 저장한다.
for row in data:
    if name in row[0]:
        print(row)
        home = np.array(row[3:], dtype=int) / int(row[2]) #row[2]=총인구수
        #string으로 저장 -> integer 타입으로 가져옴

# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
for row in data:
    away = np.array(row[3:],dtype=int) / int(row[2])
    s = np.sum((home - away) **2)
    #0에 가까울수록 유사, 음수값은 제곱해서 양수화-> 0에서 멀수록 차이큼
    if s < mn and name not in row[0]: #자기자신을 제외하고 가장 유사한 지역을 찾음
        mn = s
        result_name = row[0]
        result = away

# 5. 궁금한 지역의 인구구조와 가장 비슷한 곳의 인구구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title(name+'지역과 가장 비슷한 인구구조를 가진 지역')
plt.plot(home,label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()
