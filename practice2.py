# # 슬라이싱 예제
# hyeyeon = "960110-2134567"

# print("성별 : " + hyeyeon[7])
# print("연 : " + hyeyeon[0:2]) # 0부터 2번째 직전값 까지 (실제 자릿수보다 한자리 더)
# print("월 : " + hyeyeon[2:4]) # 01
# print("일 : " + hyeyeon[4:6]) # 10
# print("생년월일 : " + hyeyeon[:6]) # 960110 / 처음부터 6번째 직전까지
# print("뒤 7자리 : " + hyeyeon[7:]) # 2134567 / 처음부터 끝 배열까지

# print("뒤 7자리(뒤에부터) : " + hyeyeon[-7:])
# # 맨 뒤에서 7번째부터 끝까지 (음수 표기)

# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower()) # 소문자
# print(python.upper()) # 대문자
# print(python[0].isupper()) # 대문자 확인 boolean
# print(len(python)) # length. 길이 확인
# print(python.replace("Python", "Java")) # 글자 체인지

# index = python.index("n")
# print(index) # n이 몇번째 위치해 있는지 알려줌 (5)
# index = python.index("n", index + 1) # 앞에서 찾은 위치에서 하나 다음 위치에서부터 찾음
# print(index) # (15)

# print(python.find("n")) # replace랑 비슷함 (5)
# print(python.find("Java")) # 내가 원하는 값이 변수에 포함되지 않으면 -1을 반환
# #print(python.index("Java")) #컴파일 에러

# print(python.count("n")) # n이 총 몇개 있는지 카운트함 (2)

# # 문자열 포맷
# # print("a" + "b")
# # print("a", "b")

# # 1.
# print("나는 %d살입니다." % 20)
# print("나는 %s를 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# # %s는 문자와 문자열 모두 받아들일 수 있지만 %c는 문자 단위로 받아들임
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # 2.
# print("나는 {}살입니다.".format(20)) #중괄호 안에 format 함수 인자값이 들어감
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간")) # index로도 인식함
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# # 3.
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
# # 변수로도 인식함
# print("나는 {color}살이며, {age}색을 좋아해요.".format(age = 20, color = "빨간"))
# # 나는 빨간살

# # 4. (v3.6 이상부터)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# # 탈출문자
# print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈

# # 저는 "나도코딩"입니다.
# # print("저는 '나도코딩'입니다.")
# # print('저는 "나도코딩"입니다.')
# # print("저는 \"나도코딩\"입니다.") # \ : \뒤에 있는건 그 형태로 출력하겠다는 뜻

# # \\ : 문장 내에서 \로 출력
# # print("C:\\Lecture\\ShareFolder\\00_pythonWorkspace>")

# # \r : 커서를 맨 앞으로 이동
# # print("Red Apple\rPine") #PineApple

# # \b : 백스페이스(앞의 한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭(Tab)
# print("Red\tApple\tPine")

'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙 1 : http:// 부분은 제외 -> naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
                    (nav)            (5)            (1)         (!)
예) 생성된 비밀번호 : nav51!
'''
# url = "http://naver.com"
url = "http://google.com"
my_str = url.replace("http://", "") # http://를 공백 처리 - 규칙 1
my_str = my_str[:my_str.index(".")] # my_str의 . 위치 전까지만 봄 (my_str[0:5]) - 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))