print("1785103 이수연")

# if문 기본
a = 99
if a < 100:
    print("100보다 작군요.")

# list in
list = [1,2,3]
a = 1
print(a in list)

print("Korean" in ["Korean", "English"])
print("French" in ["Korean", "English"])

# 조건이 참이고 실행할 문장이 2개일 때
a = 200
if a < 100:
    print("100보다 작군요.")
    print("거짓이므로 이 문장은 안 보이겠죠?")

print("프로그램 끝")

# 들여쓰기 오류
money = 1000
water = 500
if water < money:
    print("생수를 뽑는다")
    print("물을 마신다")
    print("시원하다")

# if-else
a = 200
if a < 100:
    print("100보다 작군요.")
else:
    print("100보다 크군요.")

# 문장 여러개
a = 200
if a < 100:
    print("100보다 작군요.")
    print("참이면 이 문장도 보이겠죠?")
else:
    print("100보다 크군요.")
    print("거짓이면 이 문장도 보이겠죠?")

print("프로그램 끝")

# 입력 숫자가 짝수인지 홀수인지 계산
a = int(input("정수를 입력하세요 : " ))
if a % 2 == 0 :
    print("짝수를 입력했군요.")
else :
    print("홀수를 입력했군요.")

# if - else if
score = int(input("점수를 입력하세요 : " ))
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")
print("학점입니다. ^^")

# if - elif - else
score = int(input("점수를 입력하세요 : " ))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
print("학점입니다. ^^")

# 삼항 연산자를 사용한 if문
jumsu = 55
res = ''
res = "합격 " if jumsu >= 60 else "불합격"
print(res)