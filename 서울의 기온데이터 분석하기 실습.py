print("1785103 이수연")

## 서울의 기온 데이터 분석하기
import csv
# seoul.csv 데이터 한 행씩 읽어오기
f = open("seoul.csv", 'r', encoding = 'cp949')
data = csv.reader(f, delimiter=',') #각각의 데이터를 어떤 값을 기준으로 나눌 것인가
# for row in data:
#   print(row)  #각각의 데이터 출력

#next() 함수를 활용해 헤더 저장하기
header = next(data) #접근하는 데이터 값을 헤더로 넘겨줌
print(header)

# next() 함수를 한번 더 실행시킨 경우
line1 = next(data) # header 다음 라인 출력
print(line1)
'''
f = open("seoul.csv",'r',encoding='cp949')
data = csv.reader(f,delimiter = ',')
header = next(data) #첫번째 라인을 헤더 변수에 저장하면서 바로 제거
for row in data: #for문에서 접근하는 건 실제 데이터부터
    print(row)
'''
f.close()


# Step1. 데이터 불러서 한 행씩 출력하기
# Step2. 데이터 중 최고 기온을 실수로 변환하여 한 행씩 출력하기
f = open('seoul.csv')
data = csv.reader(f)
'''
header = next(data)
for row in data:
    row[-1] = float(row[-1]) #최고 기온을 실수로 변형
    print(row)
f.close() #오류 이유: row[-1]가 실수값이 아닌 아무값도 들어있지 않을때 실수값으로 바꿀 수 없음
'''
# Step3. 최고 기온과 최고 기온이었던 날짜 찾기
max_temp = -999 #최고 기온 값을 저장할 변수
max_date = '' #최고 기온이 가장 높았던 날짜를 저장할 변수
f = open("seoul.csv")
data = csv.reader(f)
header = next(data)

for row in data:
    if row[-1]=='':
        row[-1]=-999 #-999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1]=float(row[-1])
    if max_temp < row[-1]:  #temp값과 첫번째 행의 최고기온 값을 비교
        max_date = row[0] #max_date = 첫번째 행의 날짜값
        max_temp = row[-1] #max_temp = 비교한 기온을 넣어줌
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로,', max_temp, '도 였습니다.')
