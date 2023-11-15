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
