# for

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

#list 내의 값들을 waiting 내의 변수에 차례대로 넣는다

# for waiting_no in range(5): # 0부터 5 미만까지 (0, 1, 2, 3, 4)
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6): # 시작번호와 끝번호를 지정 (6 직전까지)
#     print("대기번호 : {0}".format(waiting_no))


# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다!!".format(starbucks))

# while

# customer = "토르"
# index = 5
#while (조건):
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1} 회".format(customer, index))
#     index += 1
# ↑ 무한루프에 빠지게 됨

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# continue와 break

# absent = [2, 5] #결석
# no_book = [7] #책을 깜빡함
# for student in range(1, 11): # 1~10번까지
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와!".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))


# 한 줄 for

#출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"] 
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"] 
# students = [i.upper() for i in students]
# print(students)

'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사다.
50명의 승객과 매칭 기회가 있을 때 총 탑승 승객 수를 구하는 프로그램을 작성하라.

조건 1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''

user = 