print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*11)
print(5>10)
print(5<10)
print(True)
print(False)
print(not True) #False
print(not False) #True
print(not (5>10)) #True

#애완동물을 소개해 주세요~

animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name +"이에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이에요")
#정수형은 print문에서 쓰이기 위해서는 str() 함수로 문자열 취급해 줘야 함
print(name, "는 ", age, "살이에요")
#, 를 쓰면 무조건 콤마를 한번 해야하고 str() 함수가 필요 없음
print("연탄이는 어른일까요? " + str(is_adult))
#문자열이 아니면 다 str() 함수로 문자열 취급해줘야 함

#주석
#이래도 되고
''' 이렇게
하면
여러문장이
주석처리
됨 '''

'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력
출력 문장 : XX행 열차가 들어오고 있습니다
'''

station = "사당"
print(station, "행 열차가 들어오고 있습니다.")
station = "신도림"
print(str(station) + " 행 열차가 들어오고 있습니다.")
station = "인천공항"
print(str(station) + " 행 열차가 들어오고 있습니다.")

#연산자

print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 5/3 한 값의 나머지 = 2n
print(10%3) # 1
print(5//3) # 5/3의 몫 = 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) #앞과 뒤의 값이 똑같다
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) #앞과 뒤의 값이 같지 않다
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True / 5는 4보다 크고, 4는 3보다 크다
print(5 > 4 > 7) # False / 5는 4보다 크고, 4는 7보다 크다

# 간단한 수식

print(2 + 3 * 4) # 14
print((2+3) * 4) # 20

number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 
print(number) # 18
number *= 2
print(number) # 36
number /= 2
print(number) # 18
number -=2 # 16
print(number)

number %= 5 # 1
print(number)

# 숫자 처리 함수
# abs = 절댓값 반환 함수
print(abs(-5)) # 5
# pow = 제곱
print(pow(4, 2)) # 4^2 = 4*4 = 16
# max = 더 큰 값 반환
print(max(5, 12)) # 12
# min = 더 작은 값 반환
print(min(5, 12)) # 5
# round = 반올림
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import * # math 라이브러리에 있는거 다 가져옴
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근, 4

#랜덤 함수
#난수, 무작위의 수

from random import *

# print(random()) # 임의의 난수를 뽑음 (0.0 ~ 1.0 미만의 임의의 값 생성)
# print(random() * 10) # 0.0~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # int 자료형으로 감싸주면 정수로 뽑아낼 수 있다
# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성

# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성

# print("random으로 값 뽑기")
# print(int(random() * 45) + 1) # 1~45까지의 임의의 값 생성
# print(int(random() * 45) + 1) # 1~45까지의 임의의 값 생성
# print(int(random() * 45) + 1) # 1~45까지의 임의의 값 생성
# print(int(random() * 45) + 1) # 1~45까지의 임의의 값 생성
# print(int(random() * 45) + 1) # 1~45까지의 임의의 값 생성
# print(int(random() * 45) + 1) # 1~45까지의 임의의 값 생성

# print("randrange로 값 뽑기")
# print(randrange(1, 46)) # 1~45 미만의 임의의 값 생성

# print("randint로 값 출력")
# print(randint(1, 45)) # a, b 사이에 있는 랜덤 숫자를 포함하는데 양 끝 숫자를 모두 포함함(1~45 이하의 값)
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))

'''
Quiz) 당신은 최근 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인, 1번은 오프라인입니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 만드세요.

조건 1 : 랜덤으로 날짜 뽑음
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
'''

day = randint(4, 28)
day2 = int((random() * 28) + 1)
day3 = randrange(1, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
# 여러 줄을 변수에 담을 수도 있다
print(sentence3)