
#Ex05_type-casting.py

'''
자료형 (data type)
-데이터를 보관하고 있는 공간의 형식을 말한다.
변수 선언과 저장을 동시에 해줘야 한다.

type()
- 변수에 저장되어 있는 데이터의 형태를 확인하는 함수.
'''

'''
bool
- True(참), False(거짓)의 값만을 가진다.
'''
ba = True
print("ba: ", ba)
print("ba type: ", type (ba))
print()

'''
int (정수)
- 양수, 음수의 숫자 값
'''
ia = -1
print("ia :", ia)
print("ia type :", type(ia))
print()

'''
float(실수)
-소수점을 사용하는 숫자 값
'''

fa = 1.2
print("fa :", fa)
print("fa type :", type(fa))
print()

'''
str(문자열)
-문자를 조합해서 사용하는 값
'''
sa = "python"
print("sa :",sa)
print("sa type: ",type(sa)) #값이 str나온다.
print()

'''
자료형변환
-데이터의 자료형을 강제로 변환 할 수 있다.
> 변환자료형(데이터)
'''

print("- bool 변환 -")
print(bool(1), bool(0), bool(-1)) #0을 제외하고 모두 true로 출력.
print(bool(1.2), bool(0.0), bool(-1.2))
print(bool(' '), bool('a'), bool(''))#공백도 문자열로 간주하게 된다. 고로 true
#그러나 아무것도 없으면 false 출력.
print()

va = 10
vb = bool(va)
print("va: {}, vb: {}".format(va, vb)) #casting을 한다고 해서 본래의 값이 변
#하는 것이 아니다. 
print()

print("- int 변환 -")
print(int(True), int(False))
print(int("123"), int("-7"))
print(int(12.34))
# print(int(a123)) -> 여기는 casting이 안된다.
print()

print("- float -")
print(float(True), float(False))
print(float("1.2"), float("-3.4")) #자료형의 ()안에는 ""로 써주거나 알아듣게 써준다.
# print(float("5.6a")) -> 이것 역시 출력되지 않는다


print("- str -")
print(str(123)) #숫자를 문자열로 바꿔준다.
a = "bcd"
print("a는",type(a))
data =123
print(data + 100)
print("data type :", type(data))

data = str(data)
# print(data + 100) 에러가 뜨는데 이건 data가 자료형이 문자열로 바뀌었기 때문이다.
print("data type:", type(data)) # 자료형이 바뀌었음을 확인할 수 있다. 
