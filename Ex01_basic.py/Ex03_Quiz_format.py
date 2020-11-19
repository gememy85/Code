#Ex03_Quiz_format.py

'''
이름, 나이, 키를 변수에 저장해서 출력하는 코드를 작성하세요
-키는 소수점 첫째자리까지만 출력
'''

'''
오늘 날짜에서 숫자만 변수에 저장해서 년월일을 출력하는 코드를 작성하세요.
-   년  월  일
'''
'''
아래의 제품이름과 가격을 각각 변수에 저장해서 출력하는 코드를 작성하세요.
---- 제 품 목 록----
bluetooth 5.0   7000
ssd 512G        120000
'''
#project no.1
name = "장원석"
age = 28
height = 170
print("이름:{}\n나이:{}\n키:{:.1f}\n".format(name, age, height))
print()

#project no.2
year = 2020
month = 11
date = 17
print("{}년 {}월 {}일".format(year, month,date))
print()

#project no.3
product1 = "bluetooth 5.0"
product2 = "ssd 512G" #문자열인데 내가 쌍또옴표 안에 넣지 않아서 실행되지 못함.
price_1 = 7000
price_2 = 120000
print("{:^30}".format("----제 품 목 록----"))
print("{:20} {:10}".format(product1,price_1))
print("{:20} {:10}".format(product2,price_2))

#######################################################################