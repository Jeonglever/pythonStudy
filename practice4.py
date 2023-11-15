# Dictionary(사전)

#cabinet = {3:"유재석", 100:"김태호"} # 사전은 중괄호로

# print(cabinet[3]) # key 값 / 유재석

# print(cabinet.get(3))
# # print(cabinet[5]) 값이 없으면 keyError 발생
# print(cabinet.get(5)) # 값이 없어도 none 취급할 뿐 계속 출력함
# print(cabinet.get(5, "사용 가능")) # 5에 값이 없으면 사용 가능이 뜸

# print(3 in cabinet) # cabinet에 3이라는 key가 있는가(boolean)
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"} # 사전은 중괄호로
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 김종국으로 A-3을 초기화
cabinet["C-20"] = "조세호"
print(cabinet)
# {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"] # A-3에 해당하는 값과 키가 삭제
print(cabinet)

# key 만 출력
print(cabinet.keys())
# dict_keys(['B-100', 'C-20'])

# value 만 출력
print(cabinet.values())
# dict_values(['김태호', '조세호'])

# key, value 쌍 출력
print(cabinet.items())
# dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

