# if
# weather = "맑아요"
# '''
# if 조건:
#     실행 명령문
# '''
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("그냥 나오셔도 됩니다~")

weather = input("오늘 날씨는 어때요? ")
'''
if 조건:
    실행 명령문
'''
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("그냥 나오셔도 됩니다~")


temp = int(input("기온은 어때요? ")) #기온이기 때문에 int로 감싸줘서 숫자 처리
if 30 <= temp:
    print("너무 덥네요 나가지 마세여")
elif 10 <= temp and temp < 30:
    print("괜찮네여 나갑시다")
elif 0 <= temp < 10:
    print("외투 챙기세요 좀 춥네용")
else:
    print("너무 추운데 나가지 마세영")
