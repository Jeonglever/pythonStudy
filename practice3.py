# 리스트 []
# 순서를 가지는 객체의 집합
# 지하철 칸별로 10명, 20명, 30명
# subway = [10,20,30]
# print(subway[0]) # 10
# print(subway) # [10, 20, 30]

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탔다
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태움
# subway.insert(1, "정형돈") # [1] index에 정형돈을 넣겠다
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop()) # 맨 뒤의 하하가 빠짐
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway) # 유재석, 정형돈 둘만 남음

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list) # 정렬되서 출력 (1,2,3,4,5)

# # 순서 뒤집기도 가능
# num_list.reverse()
# print(num_list) # (5,4,3,2,1)

# # 모두 지우기
# num_list.clear() # 배열 안의 요소들을 모두 제거
# print(num_list)

# 다양한 자료형을 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list) # mix_list를 뒤의 배열에 추가함
print(num_list)