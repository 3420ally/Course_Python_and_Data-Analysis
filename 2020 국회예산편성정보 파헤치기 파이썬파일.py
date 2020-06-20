print("1785103 이수연")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

## 자료 읽어오기
df = pd.read_csv('세출세목예산편성현황(추경포함).csv',encoding='cp949',header=0)

## 메인코드
print("반갑습니다. 2020 국회 예산 정보 파헤치기 프로그램을 시작합니다.")
while True: # -1을 입력하여 종료하기 전까지 반복하여 menu 선택 화면 실행
    menu = int(input("*본 프로그램은 -1을 입력하기 전까지 반복됩니다.\n메뉴를 선택하세요: {1:데이터 살펴보기} / {2:알고싶은 정보 찾아보기} / {-1:종료} : "))
    if menu == -1: # -1을 입력하면 프로그램 종료
        print("\n벌써요?ㅠㅠ 다음에 또 이용해주세요.\n프로그램 작성자: 경영학과 1785103 이수연\n2020-1 파이썬과 데이터분석 최종프로젝트")
        break

    if menu == 1: #1을 입력하면 데이터 살펴보기 기능 실행
        # 데이터 형태 살펴보기
        print(df.shape) #행과 열 개수
        print("2020 세출세목예산편성 데이터는 34582개의 행과 17개의 열(변수들)로 이루어져 있으며, \n각 변수들의 이름과 형태는 다음과 같습니다:")
        print(df.dtypes) #변수명 및 변수형태 알아보기

        # 정수형 변수 중 분석에 필요한 것들을 골라 배열 형태로 만든 후 연산
        df_array = np.array(df[['본예산금액(천원)', '추경정부안금액(천원)', '추경국회확정금액(천원)']])
        sum = np.sum(df_array, axis=0)  # 본예산금액, 추경정부안금액, 추경국회확정금액 각각의 합
        min = np.min(df_array, axis=0)  # 각각의 최솟값
        max = np.max(df_array, axis=0)  # 각각의 최댓값
        print('\n본예산금액의 합: ',sum[0],'원\n', '본예산금액의 최댓값: ',max[0],'원\n', '추경정부안금액의 합: ', sum[1], '원\n','추경정부안금액의 최댓값: ',max[1],'원\n',  '추경국회확정금액의 합: ', sum[2], '원\n','추경국회확정금액의 최댓값: ',max[2],'원\n')
        print('참고적으로, 최종 예산을 알 수 있는 지표는 추경국회확정금액(천원)이며,\n프로그램에서 표시되는 모든 금액은 천 원 단위입니다. ')

        # 총예산의 boxplot 그리기
        show_boxplot = int(input("총예산(추경국회확정금액)의 boxplot을 보시겠습니까? {1:예} / {2:넘어가기} : \n"))
        if show_boxplot == 1: # 1을 입력하면 추경국회확정금액의 boxplot 출력
            plt.rc('font',family="Malgun Gothic")
            plt.title('2020 대한민국 예산(국회확정금액 기준)의 상자그림')
            df.boxplot(column=['추경국회확정금액(천원)'])
            plt.show()
            plt.title('2020 예산 상자그림 _ 이상치 제거 버전')
            df.boxplot(column=['추경국회확정금액(천원)'], showfliers=False) #이상치 제거한 후 시각화
            plt.show()
            print('알고싶은 정보 찾아보기 기능으로 넘어갑니다.')

        if show_boxplot == 2: # 2를 입력하면 바로 다음 기능으로 넘어감
            print('알고싶은 정보 찾아보기 기능으로 바로 넘어갑니다.')


    if menu == 2: # 메뉴 화면에서 2를 입력하면 알고싶은 정보 찾기 기능 실행
        print("알고싶은 정보 찾기: 어떤 정보를 알고싶은가요?")

    while True: # -1을 입력하여 종료하기 전까지 반복하여 필요한 정보 선택하기 화면 실행
        search = int(input("\n*해당 기능은 -1을 입력하기 전까지 반복됩니다.\n{-1: 정보찾기 기능 종료} / {1:부처별 예산 합계 Top5} / {2:항목별 예산합계 Top5}\n{3:추경예산이 1조원 이상 편성된 지원사업 찾기} / {4:분야별 예산 차지 비중 찾기}\n{5:특정 세부사업의 본예산 & 추경금액 알아보기} / {6:특정 단위사업의 본예산 & 추경금액 알아보기} :\n" ))
        if search == -1: #-1을 입력하면 정보 찾기 기능 종료
            print("\n알고싶은 정보 알아보기 기능을 종료합니다. 이용해주셔서 감사합니다.")
            break

        if search == 1:
            # 예산이 가장 많이 배정된 기관(부처) Top5 찾기
            print("[부처별 예산 합계 Top5]")
            sum_by_org = df.groupby(['소관명'])['추경국회확정금액(천원)'].sum().sort_values(ascending=False)
            # 소관명(부처명)을 기준으로 추경국회확정금액(최종예산)의 합계 구해서 내림차순으로 정렬
            # print(sum_by_org) # 출력값이 제대로 나오는 지 확인하는 용. 프로그램 구동 시에는 필요하지 않음
            top5_org = sum_by_org.head(5)  # 추경국회확정금액(최종예산) 합계 기준 Top5 부처
            print(top5_org)

            # Top5 막대그래프로 표현
            plt.rc('font', family="Malgun Gothic")
            top5_org.plot(kind='bar') #막대그래프 그리기
            plt.title('[연간 예산이 가장 많이 편성되는 Top5 정부부처]')
            plt.show()

        elif search == 2:
            # 예산이 가장 많이 배정된 항목 Top5 찾기
            print("[항목별 예산 합계 Top5]")
            sum_by_subject = df.groupby(['목명'])['추경국회확정금액(천원)'].sum().sort_values(ascending=False)
            # 목명(예산 항목명)을 기준으로 추경국회확정금액(최종예산)의 합계 구해서 내림차순으로 정렬
            # print(sum_by_subject)
            top5_subject = sum_by_subject.head(5)  # 추경국회확정금액(최종예산) 합계 기준 Top5 항목
            print(top5_subject)


        elif search == 3:
            # 추경 예산이 1조원 이상 배정된 지원사업 찾기
            print("[추경 예산이 1조원 이상 배정된 지원사업]")
            df['추경'] = df['추경국회확정금액(천원)'] - df['본예산금액(천원)']
            # 순수 추경예산 변수 생성
            sum_by_business_extra = df.groupby(['세부사업명'])['추경'].sum()
            # 세부사업명 기준으로 추경예산 힙계 구하기
            mask1 = sum_by_business_extra > 1000000000
            # 1조원 이상에 해당하는 세부사업만 뽑아내도록 마스크 씌우기
            print(sum_by_business_extra[mask1].sort_values(ascending=False))
            # 마스크 결과를 내림차순으로 정렬

        elif search == 4:
            # 각 분야의 예산이 전체 예산에서 차지하는 비율 알아보기
            sum_by_field = df.groupby(['분야명'])['추경국회확정금액(천원)'].sum().sort_values(ascending=False)
            # 분야명을 기준으로 추경국회확정금액(최종예산)의 합계 구해서 내림차순으로 정렬
            plt.rc('font', family="Malgun Gothic")
            plt.title('[전체 예산에서 각 분야가 차지하는 비율]')
            # 파이차트 그리기
            sum_by_field.plot(kind='pie', autopct='%.1f%%')
            # 형태는 파이차트, 각 조각의 비율 표시
            plt.axis('equal')
            plt.show()

        elif search == 5:
            # 특정 세부사업의 본예산 & 추경금액 알아보기
            project_name = input('\n알고싶은 세부사업명을 입력해주세요(입력예시:코로나19): ')  # 궁금한 세부사업명 입력받기

            print('\n'+'['+project_name + "  관련 세부사업의 본예산금액]")
            origin_sum_by_project = df.groupby(['세부사업명'])['본예산금액(천원)'].sum().sort_values(ascending=False)
            # 세부사업명을 기준으로 본예산금액의 합계 구해서 내림차순 정렬
            c = origin_sum_by_project.index.str.contains(project_name)
            # 사용자가 입력한 문자열이 들어가면 True
            d = origin_sum_by_project[c]  # 입력한 문자열이 들어가는 세부사업명 및 본예산 표시
            print(d)

            print('\n'+'['+project_name + " 관련 세부사업의 추경금액]")
            sum_by_project = df.groupby(['세부사업명'])['추경국회확정금액(천원)'].sum().sort_values(ascending=False)
            # 세부사업명을 기준으로 추경예산금액의 합계 구해서 내림차순 정렬
            a = sum_by_project.index.str.contains(project_name)
            b = sum_by_project[a]  # 입력한 문자열이 들어가는 세부사업명 및 추경예산 표시
            print(b)

        elif search == 6:
            #  특정 단위사업의 본예산 & 추경금액 알아보기
            project_name2 = input('\n알고싶은 단위사업을 입력해주세요(입력예시:청년) : ')
            print('['+project_name2 + ' 관련 사업 예산]')
            origin_sum_by_unitproject = df.groupby(['단위사업명'])['추경국회확정금액(천원)'].sum().sort_values(ascending=False)
            # 단위사업명을 기준으로 예산의 합계 구해서 내림차순 정렬
            c1 = origin_sum_by_unitproject.index.str.contains(project_name2)
            d1 = origin_sum_by_unitproject[c1]  # 입력한 문자열이 들어가는 단위사업명 및 예산 표시
            print(d1)

