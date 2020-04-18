print("1785103 이수연")

#list의 개념
empty = []
number = [1, 2, 3]
strings = ["new", "face"]
numAndStr = [1, 2, 3,"new", "face"]
listInlist = [[1,3,5],[2,4,6]]

odd = [1,3,5,7,9]
odd[0]; odd[1]; odd[4]; odd[-2]
print(odd[0]);  print(odd[1]); print(odd[4]); print(odd[-1])

#list의 필요성
#변수 사용
a, b, c, d = 0, 0, 0, 0
hap = 0
a = int(input("1번째 숫자 : "))
b = int(input("2번째 숫자 : "))
c = int(input("3번째 숫자 : "))
d = int(input("4번째 숫자 : "))
hap = a + b + c + d
print("합계 == > %d" % hap)

#리스트 사용
aa = [0, 0, 0, 0]
hap = 0
aa[0] = int(input("1번째 숫자 : "))
aa[1] = int(input("2번째 숫자 : "))
aa[2] = int(input("3번째 숫자 : "))
aa[3] = int(input("4번째 숫자 : "))
hap = aa[0] + aa[1] + aa[2] + aa[3]
print("합계 == > %d" % hap)

#리스트에 원소 추가
aa = []
aa.append(0); aa.append(1); aa.append(2); aa.append(3)
print(aa)

aa = []
for i in range(0,10):
    aa.append(0)
print(aa)
print(len(aa))

##리스트와 if문
#0부터 9까지 숫자 중에서 리스트 안에 없는 숫자 찾기
import random
numbers = []
for num in range(0,10):
    numbers.append(random.randrange(0,10))
print("생성된 리스트", numbers)

for num in range(0,10):
    if num not in numbers:
        print("숫자 %d는(은) 리스트에 없네요." %num)

#기능이 두 가지인 종합 계산기 프로그램
#변수 선언 부분
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0
#메인 코드 부분
select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))
if select == 1:
    numStr = input(" *** 수식을 입력하세요 : ")
    answer = eval(numStr)
    print(" %s 결과는 %5.1f입니다." %(numStr, answer))
elif select == 2:
    num1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))
    for i in range(num1, num2+1):
        answer = answer + i
    print("%d+...+%d는 %d입니다. " %(num1, num2, answer))
else:
    print("1 또는 2만 입력해야 합니다.")

## 과제 4-1
# 숫자를 입력 받아 소수인지 아닌지 판별하는 프로그램
num = int(input("수를 입력하세요: "))
if num != 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("%d는(은) 소수가 아닙니다." % num)
            break
    else:
        print("%d는(은) 소수입니다." % num)
else:
    print("%d는(은) 소수가 아닙니다." % num)

# 리스트와 반복문
aa = []
for i in range(0,4):
    aa.append(0)
hap = 0

for i in range(0,4):
    aa[i] = int(input(str(i+1) + "번째 숫자 : " ))
    hap = hap + aa[i]
#hap = aa[0] + aa[1] + aa[2] + aa[3]
print("합계 ==> %d" %hap)

aa = []
bb = []
value = 0

for i in range(0,100):
    aa.append(value)
    value += 2
print(aa)

for i in range(99,-1,-1):
    bb.append(aa[i])
print(bb)
print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." % (bb[0], bb[99]))

#리스트 값에 접근하는 다양한 방법
aa = [10,20,30,40]
print("aa[-1]은 %d, aa[-2]은 %d" % (aa[-1], aa[-2]))
print(aa[0:3])
print(aa[2:4])
print(aa[2:])
print(aa[:2])

aa = [10,20,30]
bb = [40,50,60]
print(aa+bb)
print(aa*3)
cc = aa + bb
print("여기")
print(cc)

## 리스트값 변경
aa = [10,20,30]
print(aa)

# 두 번째에 위치한 값을 1개 변경하는 방법
aa[1] = 200
print(aa)

# 두 번째 값인 20을 300과 201이라는 값 2개로 변경하는 방법
aa[1:2] = [300,201]
print(aa)

# aa[1:2] 대신 그냥 aa[1] 사용
aa = [10,20,30]
print(aa)
aa[1] = [200,201]
print(aa)

# 두 번째인 aa[1]의 항목 삭제
aa = [10,20,30]
print(aa)
del(aa[1])
print(aa)

# 두 번째인 aa[1]에서 네 번째인 aa[3]까지 삭제
aa = [10,20,30,40,50]
print(aa)
aa[1:4] = []
print(aa)

# 리스트 자체를 삭제하는 방법
aa = [10,20,30]; print(aa)
aa = []; print(aa)

aa = [10,20,30]; print(aa)
aa = None; print(aa)

aa = [10,20,30]; print(aa); del(aa) #메모리 자체에서 삭제

## 리스트 함수
myList = [30,10,20]
print("현재 리스트: %s" % myList)

myList.append(40)
print("append(40) 후의 리스트: %s" % myList)

print("pop()으로 추출한 값: %s" % myList.pop())
print("pop() 후의 리스트: %s" % myList)

myList.reverse() #역순으로 재배열할 뿐 역순으로 sort하는 것은 아님
print("reverse() 후의 리스트: %s" % myList)

myList.sort()
print("sort() 후의 리스트: %s" % myList)

print("20 값의 위치: %d" % myList.index(20))

myList.insert(2, 222) # index(2)의 위치에 222 삽입
print("insert(2,222) 후의 리스트: %s" % myList)

myList.remove(222)
print("remove(222) 후의 리스트: %s" % myList)

myList.extend([77,88,77]) # 원래 있는 리스트에다 리스트 추가
print("extend([77,88,77] 후의 리스트: %s" % myList)

print("77 값의 개수: %d" % myList.count(77)) # 77이 몇 번 나오는 지

## 2차원 리스트
# 중첩 for 문을 사용, 3행 4열짜리 리스트 생성 후 항목 1 ~ 12를 입력하고 출력
list1 = [] # 1차원 리스트
list2 = [] # 2차원 리스트
value = 1
for i in range (0,3): # 루프 3번 반복
    for k in range (0,4): # 루프 4번 반복
        list1.append(value) # list1에 value값 [1,2,3,4] [5,6,7,8] [9,10,11,12] 집어넣기
        value += 1
    list2.append(list1)
    print(list2)
    list1 = []

for i in range(0,3):
    for k in range(0,4):
        print("%3d" % list2[i][k], end = " ")
    print("")