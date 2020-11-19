
#Ex06_Quiz_input.py

'''
ID 를 입력받고, 입력받은 ID를 사용해서 E-mail 주소를 생성하는 코드를 작성하라.

이름, 나이, 전화번호를 입력받아서 출력하는 코드를 작성하세요.

숫자 2개를 입력받아서 사칙연산(+,-,*(곱),/(나눗셈))
결과를 출력하는 코드를 작성하라. 

태어난 년도를 입력 받아서 나이를 계산하는 코드를 작성하라.

키를 입력받아서 표준체중을 구하는 코드를 작성하라.
- 표준체중 = (키 - 100)* 0.9
'''

# dataA = input("ID를 입력하세요: ")
# print("Email은 :{}@naver.com입니다.".format(dataA))
# print()

# dataA = input("ID 입력 : ")
# domain = "@naver.com"
# usermail = dataA + domain
# print("Email은 : {}". format(usermail))

name = input("이름 입력 : ")
age = input("나이 입력 : ")
phone = input("전화번호를 입력하세요 : ")
print('''이름은 {}\n
나이는 {}\n
전화번호는 {}\n'''.format(name, age, phone))
print()

# dataB = input("숫자 2개를 입력하시오: ")
# d1, d2 = dataB.split()
# d1, d2 = int(d1), int(d2) #이렇게 쓰는 것은 가능하다. 
# print("합 : {}\n차 : {}\n곱 : {}\n나눗셈 : {:.1f}".format(d1+d2,d1-d2,d1*d2,d1/d2))
# print()

# dataC = int(input("출생년도를 입력하세요: "))
# Age = 2020 - dataC
# print("당신의 나이는 : {} ".format(Age))
# print()

# dataD = float(input("키를 입력하세요: "))
# print("당신의 표준체중은 : {:.1f} ". format((dataD-100)*0.9))