# # Ex03_Format.py

# '''
# format() 메소드
# -print("{}".format(데이터))
# > 쌍따옴표안의 {}(포맷필드) 위치에 데이터를 출력한다.
# '''
# dataA = 100
# print("dataA: ", dataA)
# print("dataA: {}".format(dataA))
# print()

# dataB = 200
# print("dataB: ", dataB)
# print("dataA:", dataA, ",dataB: ",dataB)
# print("dataA: {}, dataB {}". format(dataA, dataB)) #쓰기가 훨씬 쉽다. 

# year = 2020
# title = "python"
# print("제목 : {} - 출판년도 : {}". format(title,year))#중괄

##############################################################################

'''
소수점 자리 조정
-{ : .소수점자리f}
>지정한 소수점 자리까지 출력한다. 
'''

height = 123.1234
print("높이 :{}". format(height))
print("높이 :{:.1f}".format(height)) #소수점 첫번째 자리까지만 출력.

'''
출력 필드 폭 지정
-{:정수}
> 정수값 만큼의 공간확보를 하고 데이터를 출력

-{: 기호 정수}
> 기호: 숫자는 기본이 오른쪽 맞춤이고, 문자열은 기본이 왼쪽 맞춤
 < : 왼쪽 맞춤
 ^ : 가운데 맞춤
 > : 오른쪽 맞춤
'''

value =123
print("{}".format(value))
print("{:5}".format(value)) #숫자는 기본이 오른쪽 맞춤

print("{:<5}#".format(value))
print("{:^5}#".format(value))
print()

word = 'abc'
print("{}".format(word))
print("{:5}".format(word))#문자는 기본 왼쪽 맞춤.
print("{:<5}#".format(word)) #왼쪽 맞춤
print("{:^5}#".format(word)) #가운데 맞춤
print()

####################################################################

'''
진법 변환
-{:b} 2진수
 {:o} 8진수
 {:x} 16진수
'''
ten = 10
print("ten : ", ten)
print("2진수 : {:b}".format(ten))
print("8진수 : {:o}".format(ten))
print("16진수 : {:x}".format(ten))