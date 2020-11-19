
#Ex04_string.py

# '''
# 문자열
# -문자 데이터 여러개의 집합.
# '''

# print('문자열')
# print("문자열")
# print('''외따옴표 3개를 사용하면 여러
# 줄의 문자열을 한번에 출력할 수 있다
# 하하''') #이렇게 하면 컴퓨터가 라인변경을 인식해서 출력이 된다. 

'''
문자열 연산
-숫자처럼 문자열끼리도 서로 더하거나 곱할 수 있다.
'''
textA = "smile"
textB = "^^"
print("textA: ",textA)
print("textB: ",textB)

stn = textA + " " + textB #이런식으로 합쳐서 출력이 가능하다. 
print("stn : ",stn)
print(textA+textB) #이런식으로도 되는데 띄어쓰기가 되진 않는다. 
print(textA * 2) #이럴 경우 두번 출력된다. 띄어쓰기는 되지 않는다. 

'''
문자열은 문자들의 집합이기 때문에 특정위치의 문자를 선택해서 사용 할 수 있다.
-각 문자에는 index(번호)가 부여된다.
-index는 0부터 시작해서 1씩 증가한다.
-Ex) 변수명 [index]
'''
# +       0123456 7 8 9
nation = "korea 대한민국"
# -      1098765 4 3 2 1 ->이건 파이썬에서만 가능. 
print("nation : ",nation)
print("nation[0] :", nation[0])
print("nation[6] :", nation[6])
print("nation[-3] :", nation[-3])