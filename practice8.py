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

for waiting_no in range(1, 6): # 시작번호와 끝번호를 지정 (6 직전까지)
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다!!")