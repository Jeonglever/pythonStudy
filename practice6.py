# # 자료구조의 변경
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # set

# menu = list(menu) # list로 감쌈
# print(menu, type(menu)) # list

# menu = tuple(menu)


# print(menu, type(menu)) # tuble


# menu = set(menu)
# menu.add("식혜")
# print(menu)


'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명을 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건 1 : 편의상 댓글은 20명이 작성, 아이디는 1~20이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위 추첨이되 중복은 불가
조건 3 : random 모듈의 shuffle과 sample 을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
'''

from random import *

# lst = []
# for a in range(20):
#     lst.append(a+1)

lst = range(1, 21) # 1부터 21 직전까지(20) 숫자 생성
lst = list(lst) # 을 리스트화 시킴
# print(type(lst)) # list로 출력됨
shuffle(lst)
winners = sample(lst, 4)


print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")
