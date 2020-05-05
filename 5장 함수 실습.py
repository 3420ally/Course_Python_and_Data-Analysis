print("1785103 이수연")

# 함수를 사용하지 않을 경우
coffee = 0
coffee = int(input("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙)"))
print()
print("# 1. 뜨거운 물을 준비한다.");
print("# 2. 종이컵을 준비한다.");

if coffee == 1:
    print("# 3. 보통커피를 탄다.")
elif coffee ==2:
    print("# 3. 설탕커피를 탄다.")
elif coffee ==3:
    print("# 3. 블랙커피를 탄다.")
else:
    print("# 3. 아무거나 탄다.\n")

print("# 4. 물을 붓는다.");
print("# 5. 스푼으로 젓는다.");
print()
print("손님~ 커피 여기 있습니다.^^")

# 함수를 사용한 경우
# 전역변수 선언 부분#
coffee = 0

# 함수 선언 부분#
def coffee_machine(button):
    print()
    print("# 1. (자동으로) 뜨거운 물을 준비한다.");
    print("# 2. (자동으로) 종이컵을 준비한다.");

    if button == 1:
        print("# 3. (자동으로) 보통커피를 탄다.")
    elif button == 2:
        print("# 3. (자동으로) 설탕커피를 탄다.")
    elif button == 3:
        print("# 3. (자동으로) 블랙커피를 탄다.")
    else:
        print("# 3. (자동으로) 아무거나 탄다.\n")

    print("# 4. (자동으로) 물을 붓는다.");
    print("# 5. (자동으로) 스푼으로 젓는다.");
    print()

# 메인코드 부분#
coffee = int(input("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙)"))
coffee_machine(coffee)
print("손님~ 커피 여기 있습니다.^^")

coffee = int(input("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙)"))
coffee_machine(coffee)
print("손님~ 커피 여기 있습니다.^^")

## 실습 1: return값이 없는 함수
# 함수 정의
def workinfo(name,money):
    print("가게: "+name)
    print(("시급: ", money, "원"))
    print("시간: 오전 10시 ~ 오후 5시")
    print("요일: 월 ~ 금요일")
# 함수 호출
workinfo("김밥낙원", 7530)

## 실습 2: return값이 있는 함수
def CalcBMI(weight, height):
    BMI = weight/height**2*10000
    return BMI
print(CalcBMI(55,155))

## 실습 3: return값이 있는 함수
# 함수 선언 부분 #
def plus(v1,v2):
    result = 0
    result = v1 + v2
    return result
# 전역변수 선언 부분 (프로그램 전체에서 사용) #
hap = 0
# 메인코드 부분 #
hap = plus(100,200)
print("100과 200의 plus() 함수 결과는 %d" % hap)

## 실습 4: 커피 자판기
def coffeeMachine(money,name):
    if name == "아메리카노":
        price = 1500
        print("아메리카노가 나왔습니다.")
    elif name == "에스프레소":
        price = 1000
        print("에스프레소가 나왔습니다.")
    elif name == "밀크티":
        price = 2000
        print("밀크티가 나왔습니다.")
    else:
        price = 0
        print(name + "는 없습니다.")

    change = money - price
    return change

print(coffeeMachine(2000,"아메리카노"))
print(coffeeMachine(2000,"밀크티"))
print(coffeeMachine(3000,"카페라떼"))

## 실습 5: 덧셈, 뺄셈, 곱셈, 나눗셈을 하는 계산기 함수를 작성
# 함수 선언 부분 #
def calc(v1,v2,op):
    result = 0
    if op == "+":
        result = v1 + v2
    elif op == "-":
        result = v1 - v2
    elif op == "*":
        result = v1 * v2
    elif op == "/":
        result = v1 / v2
    return result
# 전역변수 선언 부분 #
res = 0
var1, var2, oper = 0, 0, ""
# 메인코드 부분 #
oper = input("계산을 입력하세요(+, -, *, /) : ")
var1 = int(input("첫번째 수를 입력하세요: "))
var2 = int(input("두번째 수를 입력하세요: "))
res = calc(var1, var2, oper)
print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))

## 실습 6: 지역변수와 전역변수의 이해
# 함수 선언 부분 #
def func1():
    a = 10 # 지역변수
    print("func1()에서 a값 %d" % a)

def func2():
    print("func2()에서 a값 %d" % a)

# 전역변수 선언 부분 #
a = 20 # 전역변수

# 메인코드 부분 #
func1()
func2()

## 실습 7: 반환값이 여러 개인 함수
# 함수 선언 부분 #
def multi(v1,v2):
    retList = [] #반환할 리스트
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

# 전역 변수 선언 부분 #
myList = []
hap, sub = 0, 0

# 메인 코드 부분 #
myList = multi(100,200)
hap = myList[0]
sub = myList[1]
print("multi()에서 돌려준 값 --> %d, %d" % (hap, sub))

## 실습 8: global 예약어
# 함수 선언 부분 #
def func1():
    global a # 이 함수 안에서 a는 전역변수. 지역변수로 바뀌지 않음
    a = 10
    print("func1()에서 a값 %d" %a)

def func2():
    print("func2()에서 a값 %d" %a)

# 함수 변수 선언 부분 #
a = 20 #전역 변수
# 메인 코드 부분 #
func1()
func2()

## 파이썬 내장함수
# 문자열 관련 함수
# 실습9
print("hello".find("l")) # hello에서 l이 첫번째 나온 위치 index 번호
print("hello".find("p")) # 없음 -> -1
print("hello".index("l"))
#print("hello".index("p")) # 없음 -> 오류

# 실습 10
print("-".join("hello")) # hello 사이에 - 넣음
print(("h#e#l#l#o".split("#"))) # 문자열을 # 기준으로 나눔
print("My name is Python".split(" ")) # 빈공간 기준으로 나눔
print("My name is Python".split()) # 디폴트가 빈공간 기준

# 실습 11 : 문자열 검사
print("293fnc".isalnum()) #number나 alphabet이면 true
print("412csa#@$".isalnum()) #특수기호 들어가면 false
print("asfc".isalpha()) #문자로만
print("이보영".isalpha())
print("3124".isdigit()) #숫자로만
print("3124dasfd".isdigit())

# 실습 12 : 문자열 변환
print("ABC".isupper())
print("abc".islower())
print("hello".upper()) #대문자로 변환
print("HELLO".lower())
print("hello".replace("l","L"))
print("hello".replace("l","L",1)) #첫번째 l만 수행

# 실습 13 : 수치 계산을 위한 내장 함수
print(max(1,2,3))
print(max([1,2,3]))
print(abs(-5)) #절댓값
print(sum([1,2,3])) #0에서부터 1,2,3 더함
print(sum([1,2,3],2)) #2에서부터 1,2,3 더함
print(pow(2,3)) #2의 3제곱
print(pow(2,3,5)) #2의 3제곱을 5로 나눈 나머지
print(round(1.2))

# 실습 14 : math 모듈 내 수학 함수
import math
print(math.log(4))
print(math.log(4,2))
print(math.sqrt(9))
print(math.sin(math.radians(90)))
print(math.cos(math.radians(180)))
print(math.pi)
print(math.sin(math.pi/2))
print(math.cos(math.pi))

# 실습 15 : math 모듈의 어림 함수
import math
print(math.ceil(1.4)) #올림
print(math.ceil(-1.4))
print(math.floor(1.4)) #버림
print(math.floor(-1.4))
print(math.trunc(1.2)) #반올림
print(math.trunc(-1.2))

## 과제 5-1 : 문자열 압축하기
# 함수 이름: StringZip
# 압축할 문자열을 사용자로부터 입력받는다.
# 테스트 문자열: "aaaaabbbbbccccccaaaddddd"
# 다음문자와 같으면 count+1, 다음문자와 다르면 거기까지의 결과 출력

# 방법1
s = input("문자열을 입력하세요: ") # 사용자로부터 문자열 입력 받아 저장

def StringZip():
    result = ""  # 결과 변수
    count = 0  # 반복수를 세는 변수
    for i in s: # 문자열의 각 단어를 순서대로 i로 받아옴
        if result == "":  #첫번째 글자라면 result에 첫번째 글자 입력, 개수+1
            result = i
            count += 1
        elif result == i:  #연속된 글자라면 개수만 증가
            count += 1
        else:    #앞에 세던 글자와 다르다면
            print(result+str(count),end="")   #지금까지 세던 글자를 출력하고
            result = i    #새로운 글자를 센다
            count = 0
            count += 1
    result += str(count)  # 마지막 글자의 결과까지 출력
    print(result)

print(StringZip())

# 방법2
s = input("문자열을 입력하세요: ")  # 사용자로부터 문자열 입력 받아 저장

def StringZip(s):
    result = s[0]
    count  = 0
    for i in s:  # 문자열의 각 글자를 순서대로 i로 받아옴
        if i == result[-1]:  # i 글자가 이전 글자와 같다면 count+1
            count += 1
        else:  # i 글자가 이전 글자와 다르다면
            result += str(count) + i  # 이전 글자의 반복수를 출력하고 i 글자 출력
            count = 1  # 이때 새로운 글자의 반복수는 1이 디폴트
    result += str(count)  # 마지막 글자의 결과까지 출력
    print(result)

print(StringZip(s))







