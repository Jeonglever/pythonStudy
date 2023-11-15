# Tuple (튜플)
# 리스트하고는 다르게 내용의 변경, 추가가 불가능
# 그렇지만 속도는 리스트보다 빠름
# 변경되지 않는 목록을 사용할 때 사용

menu = ("돈까스", "치즈까스") # 소괄호
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 컴파일 에러

# name = "정혜연"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


# Set (집합)
# 중복이 안됨, 순서 없음
my_set = {1,2,3,3,3} # Set도 사전처럼 중괄호로 쓰고, 값만 쭉 나열하면 됨
print(my_set) # {1,2,3} 출력

java = {"정혜연", "김태호", "양세형"}
python = set(["정혜연", "박명수"])

# 교집합 (Java와 python을 모두 할 수 있는 개발자)
print(java & python) # 정혜연
print(java.intersection(python)) # 정혜연

# 합집합 (java 도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python) # 김, 양, 박, 정...
print(java.union(python)) # 김, 양, 박, 정...
# 순서가 보장되지 않고 집합에 있기에 그냥 빼내서 출력함

# 차집합 (java는 할 줄 알지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))
# 양세형, 김태호 ...

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # 정혜연, 박명수, 김태호

# java 까먹
java.remove("김태호")
print(java)

