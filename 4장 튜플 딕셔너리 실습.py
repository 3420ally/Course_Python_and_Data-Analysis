print("1785103 이수연")

## 튜플의 생성 - 읽기 전용 데이터. 수정 불가
tt1 = (10,20,30); print(tt1)
tt2 = 10,20,30; print(tt2)

tt3 = (10); print(tt3) # 원소만 저장
tt4 = 10; print(tt4)
tt5 = (10,); print(tt5) # 튜플 저장
tt6 = 10, ; print(tt6)

## 튜플의 오류 - append 또는 기존의 값 변경 불가
#tt1.append(40); print(tt1)
#tt1[0] = 40; print(tt1)

## 튜플의 삭제
del(tt1) # 완전히 삭제 -> 정의되지 않음
print(tt1)

## 튜플의 사용
# 튜플 항목에 접근
tt1 = (10,20,30,40)
print(tt1[0])
tt1[0]+tt1[1]+tt1[2]

# 튜플 범위에 접근
print( tt1[1:3] )
print( tt1[1: ] )
print( tt1[ :3] )

tt2 = ("A", "B")
print(tt1+tt2)
print(tt2*3)

## 튜플 -> 리스트 -> 튜플 변환
myTuple = (10,20,30)
myList = list(myTuple)
print(myList)
myList.append(40)
print(myList)
myTuple = tuple(myList)
print(myTuple)

## 과제2
# 다음과 같은 이차원 튜플을 생성한 후 모든 값을 각각 출력해보자.
list1 = [] # 1차원 리스트
list2 = [] # 2차원 리스트
value = 1
for i in range (0,3): # 루프 3번 반복
    for k in range (0,3): # 루프 4번 반복
        list1.append(value) # list1에 value값 [1,2,3] [4,5,6] [7,8,9] 집어넣기
        value += 1
        tuple1 = tuple(list1)
        #print(tuple1)
    list2.append(tuple1)
    tuple2 = tuple(list2)
    list1 = []
print(tuple2)

for i in range(0,3):
    for k in range(0,3):
        print("%3d" % tuple2[i][k], end = " ")
    print("")

## 딕셔서리의 생성
dic1 = {1:"a", 2:"b", 3:"c"}
print(dic1)
dic2 = {"a":1, "b":2, "c":3}
print(dic2)

## 여러 정보의 딕셔너리 표현
student1 = {"학번":1785103, "이름":"이수연", "학과":"경영학과",}
print(student1)

# student1에 연락처 추가
student1["연락처"] = "010-1234-5678"
print(student1)

# 학과 수정
student1["학과"] = "소프트웨어전공"
print(student1)

# student1의 학과 삭제
del(student1["학과"])
print(student1)

student1 = {"학번":1785103, "이름":"이수연", "학과":"소프트웨어전공","학번":1701001}
print(student1) # 중복되는 데이터는 뒤의 값이 앞의 값을 덮어쓰기
print(student1["학번"])
print(student1["이름"])
print(student1["학과"])

# 딕셔너리명.get(key) 함수를 사용해 key로 값에 접근
print(student1.get("이름"))

# 없는 키를 찾을 때 딕셔너리명.get(key)를 사용
#print(student1["주소"]) #오류 발생
print(student1.get("주소")) #오류X, 그냥 반환값X(None)

# 딕셔너리명.keys()는 딕셔너리의 모든 키 반환
print(student1.keys())
print(list(student1.keys()))
print(student1.values())

#딕셔너리명.items() 함수를 사용하면 튜플 형태로도 구할 수 있음
print(student1.items())
print("이름" in student1) #결과->True/False
print("주소" in student1)

# for문을 활용해 딕셔너리의 모든 값을 출력
singer = {}
singer["이름"]="트와이스"
singer["구성원수"]=9
singer["데뷔"]="서바이벌 식스틴"
singer["대표곡"]="TT"

for k in singer.keys():
    print("%s --> %s" % (k, singer[k]))

## 딕셔너리의 정렬
# key로 정렬한 후 딕셔너리 추출
import operator
trainDic, trainList = {}, []
trainDic = {"Thomas": "토마스","Edward": "에드워드","Henry": "헨리","Gothen": "고든","James": "제임스"}
trainList = sorted(trainDic.items(), key=operator.itemgetter(0)) # 앞에 있는 key를 기준으로 정렬
print(trainList)
print(trainDic)

## 딕셔너리를 활용해 음식 궁합을 출력하는 프로그램
# 변수 선언 부분
foods = {"떡볶이":"오뎅", "짜장면":"단무지", "라면":"김치",
         "피자":"피클", "맥주":"팝콘", "치킨":"치킨무", "삼겹살":"상추"}

# 메인 코드 부분
while(True):
    myfood = input(str(list(foods.keys()))+"중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s> 과 궁합이 맞는 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝":
        break
    else:
        print("그런 음식이 없습니다. 확인해 보세요.")
