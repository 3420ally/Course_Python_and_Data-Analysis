
# 원주와 원의 넓이 구하기
print("1785103 이수연")
radius = int(input("반지름은? "))
area = 3.14*radius**2
circum = 2*3.14*radius
print("넓이는 ", area, "이고, 원주는 ", circum, "이다")

# 지하철 자동 발권 프로그램
print("1785103 이수연")
money = int(input(" 투입한 돈은? "))
course1 = int(input("1구간 표의 수는? "))
course2 = int(input("2구간 표의 수는? "))
change = money - course1*700 -course2*900
print("잔돈: ", change, "원")
change1000 = change//1000
change = change%1000
change100 = change//100
print("1000원 지폐: ", change1000, "장")
print("100원 동전: ", change100, "개")