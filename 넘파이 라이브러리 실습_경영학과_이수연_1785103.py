print("1785103 이수연")
'''
## 1. Matplotlib 홈페이지
# 리스트와 Numpy 비교
# 리스트를 활용해 작성한 코드
import matplotlib.pyplot as plt
t = []
p2 = []
p3 = []
for i in range (0,50,2):
    t.append (i/10)
    p2.append ((i/10)**2)
    p3.append ((i/10)**3)
plt.plot(t,t,'r--', t, p2, 'bs', t, p3, 'g^')
# x,y좌표값 t -> 빨간 대시 선 / x좌표 t, y좌표 p2 -> 파란  네모 선 / x좌표 t, y좌표 p3 -> 초록 세모 선
plt.show()

# Numpy를 활용해 작성한 코드
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 5., 0.2) #시작점, 끝점, 간격
plt.plot(t,t,'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show() # 위와 동일한 그래프
'''
## 2. Numpy 라이브러리 시작하기
# 제곱근 출력하기
import numpy as np
'''
print(np.sqrt(2))

# 파이와 삼각함수 활용하기
print(np.pi)
print(np.sin(0))
print(np.cos(np.pi))

## 3. numpy 라이브러리를 활용해 그래프 그리기
# random 서브 라이브러리의 rand 함수 / numpy의 ndarray 타입
a = np.random.rand(5) #0에서부터 5까지의 실수 random으로 만들기
a = np.random.rand(0, 10, 5) #0에서 10 사이 random값 5개
print(a)
print(type(a))

# random 서브 라이브러리의 choice 함수
print(np.random.choice(6,10)) #6보다 작은 정수값 10개 생성
# random 서브 라이브러리의 choice 함수(중복금지)
print(np.random.choice(10, 6, replace = False))
#10보다 작은 정수 6개 생성, 발생되는 숫자들은 중복되지 않게
# random 서브 라이브러리의 choice 함수(확률 설정)
print(np.random.choice(6,10, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1]))
# p = 각각 0,1,2,3, ... 가 발생할 확률. 확률 합쳐서 1이 되어야함

# random을 사용해 히스토그램 그리기
import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6,10) #0에서 6까지 10개
print(dice)
plt.figure(dpi=300)
plt.hist(dice,bins=6)
plt.show()

# 랜덤 확률이 설정된 히스토그램 그리기
# random을 사용해 히스토그램 그리기
import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6,1000000, p=[0.1,0.2,0.3,0.2,0.1,0.1]) #각 확률을 따라감
print(dice)
plt.figure(dpi=300)
plt.hist(dice,bins=6)
plt.show()

## 4. numpy array 생성하기
# 리스트로 ndarray(N-Dimensional Array) 만들기
a = np.array([1,2,3,4])
print(a) # 결과 [1,2,3,4] 각각의 원소가 콤마 아닌 띄어쓰기로 구분

# numpy array의 인덱싱, 슬라이싱
print(a[1], a[-1]) # 결과 2 4
print(a[1:]) # 결과 [2,3,4]

# zeros(), ones(), eye() 함수로 numpy array 만들기
a = np.zeros(10) #0으로 이루어진 크기가 10인 배열 생성
print(a)

a = np.eye(3) # 3x3의 단위행렬(대각선이 1이고 나머지원소 0) 생성
print(a)

# 연속된 숫자의 numpy array 만들기 -정수만 생성
import numpy as np
print(np.arange(3))
#arrange() 함수에 1개 값 입력 -> 0에서 3까지 1씩 증가
print(np.arange(3,7))
#arrange() 함수에 2개 값 입력 -> 3이상 7미만 1씩 증가
print(np.arange(3,7,2))
#arrange() 함수에 3개 값 입력 -> 3이상 7미만 2씩 증가

# 연속된 실수의 numpy array 만들기
a = np.arange(1,2,0.1) #0부터 9까지 0.1 간격의 연속된 숫자 생성
b = np.linspace(1,2,11) #1부터 2(2도 포함)를 11개의 구간으로 나눈 실수 생성
print(a)
print(b)

# 연속된 실수의 numpy array 만들기
a = np.arange(-np.pi, np.pi, np.pi/10)
b = np.linspace(-np.pi, np.pi, 20) #pi값도 포함
print(a)
print(b)

## 5. numpy array의 다양한 활용
# numpy array에 값을 한꺼번에 더하기
a = np.zeros(10) + 5 #크기가 10이고 각 원소가 0인 배열 생성 -> 각 원소에 5를 더함
print(a)

# numpy array에 함수 적용하기
a = np.linspace(1,2,11)
print(np.sqrt(a)) #각 원소에 sqrt

# Numpy를 활용한 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi=300)
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()

# 다양한 그래프 그리기
plt.figure(dpi=300)
plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a + np.pi/2, np.sin(a)) #pi/2만큼 이동
plt.show()

# Mask 적용하기 _기본 데이터 만들기
import numpy as np
a = np.arange(-5,5)
print(a)

# Mask 적용하기 _마스크 만들기
print(a<0) #0보다 작으면 True, 0이상이면 False
print(a[a<0]) #a에서 True인 것들만 출력

# Mask 적용하기 _마스크 적용하기
mask1 = abs(a)>3
print(mask1)
print(a[mask1])

# Mask 적용하기 _마스크 연결해서 사용하기
mask1 = abs(a)>3
mask2 = abs(a) % 2 == 0
print(mask1) #3 초과 True
print(mask2) #2의 배수 True
print(a[mask1 + mask2]) #둘 중 하나의 조건이라도 참일 경우 출력
print(a[mask1 * mask2]) #두 가지 조건이 모두 참일 경우 출력
'''
## Numpy 라이브러리를 사용하여 재미있는 버블차트 그리기
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(-100,100,1000) #1000개의 랜덤값 추출
y = np.random.randint(-100,100,1000)
size = np.random.rand(100)*100

mask1 = abs(x)>50 #x에 저장된 값 중 절댓값이 50보다 큰 값 걸러냄
mask2 = abs(y)>50
x = x[mask1 + mask2] #mask1과 2 중 하나라도 만족하는 값 저장
y = y[mask1 + mask2]

# 수정한 부분
num = len(x)
size = np.random.rand(num)*100

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()



