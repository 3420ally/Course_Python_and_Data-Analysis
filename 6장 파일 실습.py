print("1785103 이수연")
## 파일 입출력
'''
# 파일 쓰기
f = open("c:/python/food.txt",'w') #파일 열기
f.write("떡볶이\n")
f.write("피자\n")
f.close()

# 파일 읽기
f = open("c:/python/food.txt",'r')
data = f.read()
print(data)
f.close()

f = open("c:/python/food.txt",'r')
line1 = f.readline()
print(line1)
print(line1, end = '')
line2 = f.readline()
print(line2)
f.close()

f = open("c:/python/food.txt",'r')
list = f.readlines()
print(list)
f.close()

# 파일 쓰기
f = open("c:/python/food.txt",'a') #절대경로로 생성
f = open("food.txt",'a') #상대경로로 생성, '6장 파일 실습'과 같은 위치에 저장
f.write("파스타\n")
f.close()

## 메모장 프로그램
def write_your_memo(mode):
    f = open('memo.txt', mode)
    memo = input('Input your memo> ') + '\r\n'
    f.write(memo)
    f.close()

mode = input('w : New memo note, a : Append your memo ? ')

if mode == 'w' or mode == 'a':
    write_your_memo(mode)
    if mode == 'w':
        print('Wrote your memo to a new note.')
    else:
        print('Appended your memo.')
else:
    print('Wrong command')

# 여러 개의 메모지 만들기
def write_your_memo(file_name, mode):
    f = open(file_name, mode)
    memo = input('Input your memo> ') + '\r\n'
    f.write(memo)
    f.close()

file_name = input('input memo name > ') #사용자로부터 입력받은 변수명
mode = input('w : New memo note, a : Append your memo ? ')
print(mode)

if mode == 'w' or mode == 'a':
    write_your_memo(file_name, mode)
    if mode == 'w':
        print('Wrote your memo to a new note.')
    else:
        print("Append your memo.")

## 과제 6-1: 메모장 만들기
조건1. 메모를 저장하는 기능과 읽어오는 기능을 가진다.
        메뉴1 메모를 저장하기 2 메모를 읽어오기 -1 프로그램 끝내기
        프로그램 끝내기를 선택할 때까지 반복해서 동작
조건2. 여러 개의 메모장을 만들고 내용을 추가할 수 있어야한다.
조건3. 파일명을 입력하면 메모장의 내용을 읽어 화면에 출력한다.(readline 함수 사용)
        존재하는 파일만을 읽는다고 가정한다.
조건4. 메뉴1과 메뉴2의 기능은 각각의 함수로 구현한다.

구현: 메모장 프로그램을 시작합니다
메뉴를 선택하세요
메뉴 1 메모를 저장하기 2 메모를 읽어오기 -1 프로그램 끝내기
'''
print("메모장 프로그램을 시작합니다")
menu = int(input("메뉴를 선택하세요:: (1:메모 저장하기) (2:메모 읽기) (-1:종료) "))
print(menu)

def write_memo(file_name, mode):
    f = open(file_name, mode)
    memo = input('Write your memo: ') + '\r\n'
    f.write(memo)
    f.close()

file_name = input('저장하려는 메모의 이름을 입력하세요: ')
mode = input('w : 새로 쓰기 / a : 기존 메모에 추가하기 ')
if mode == 'w' or mode == 'a':
    print(write_memo(file_name, mode))
    if mode == 'w':
        print('Wrote your memo to %s.' % file_name)
    else:
        print("Appended your memo to %s." % file_name)
else:
    print('Wrong Command.')

def read_memo(file_name2):
    f = open(file_name2,'r')
    line1 = f.readline()
    print(line1, end='')
    line2 = f.readline()
    print(line2, end='')
    f.close()

file_name2 = input('찾으려는 메모의 이름을 입력하세요: ')

## 메인코드
while not menu == -1:
    if menu == 1:
        write_memo(file_name, mode)
        pass
    elif menu == 2:
        read_memo(file_name2)
        pass
    elif menu == -1:
        print("메모 프로그램을 종료합니다.")
        break
    else:
        print("해당 메뉴가 없습니다. 메뉴를 다시 한번 확인하세요.")
