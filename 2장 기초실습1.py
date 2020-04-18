print("1785103 이수연")
print("Hello World!")

# 실습1
print("1785103 이수연")
eng = input("영어 점수를 입력하시오:")
math = input("수학 점수를 입력하시오:")
totalScore = eng + math
print("총점 = ", totalScore)

eng = int(input("영어 점수를 입력하시오:"))
math = int(input("수학 점수를 입력하시오:"))
totalScore = eng + math
print("총점 = ", totalScore)

name = input('이름을 입력하시오:')
print(name + '님 반갑습니다.')
''''''
# 실습2 (연산)
print("1785103 이수연")
a = 100; b = 50
result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)
result = a * b
print(a, "*", b, "=", result)
result = a / b
print(a, "/", b, "=", result)
''''''

# 실습3 (Bool형)
print("1785103 이수연")
a = True
type(a)

print(a)
print(type(a))

a = (100 == 100)
b = (10 > 100)
print(a, b)
''''''
# 실습4 (문자형)
print("1785103 이수연")
a = "파이썬 만세"
print(a); type(a)

"작은따옴표는 ' 모양이다"
'큰따옴표는 " 모양이다'
print("작은따옴표는 ' 모양이다")
print('큰따옴표는 " 모양이다')

a = "이건 큰따옴표는 \" 모양이다"
b = '이건 작은따옴표는 \' 모양이다'
print(a, b)

a = '파이썬 \n만세'
print(a)

a = """파이썬
만세"""
print(a)

a = '1$ 환율은 1100입니다.'
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
print(a[7:11])
''''''
# 실습5 (수식의 표현)
print("1785103 이수연")
a = 5; b = 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)
''''''
# 실습6 (산술 연산과 문자열)
print("1785103 이수연")
s1, s2, s3 = "100", "100.123", "9999999999"
print(int(s1)+1, float(s2)+1, int(s3)+1)
# print(s1+1, s2+1, s3+1)
print(s1+"1", s2+"1", s3+"1")
''''''
# 실습7 (산술 연산과 문자열)
print("1785103 이수연")
a = 100; b = 100.123
str(a) + '1'; str(b) + '1'
print(str(a) + '1', str(b) + '1')
''''''
# 실습8 (관계 연산자)
print("1785103 이수연")
a, b = 100, 200
print(a == b, a != b, a > b, a < b, a >= b, a <= b)
''''''
# 실습9 (논리 연산자)
print("1785103 이수연")
a = 100
print((a > 100) and (a < 200))


