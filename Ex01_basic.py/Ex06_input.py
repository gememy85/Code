

#Ex06_imput.py


'''
input()
-키보드로 입력한 값을 프로그램에게 전달한다.
'''
# print("데이터 입력 > ", end="")
# va = input()#이걸 돌리면 콘솔창이 뜨고 거기에 데이터를 입력하고 Enter를 누르면 저장된다.
# print("va : ", va)
# print()

'''input 함수의 () 안에 출력 할 내용을 작성 할 수 있다.
'''
# vb = input("키보드 입력 >") #고로 print문을 따로 작성할 필요가 없다. 엄청 편하지 않은가.
# print("vb : ",vb)
# print()

'''
input 함수로 입력한 데이터는 모두 문자열로 처리 된다.!!
'''

# vc = input("키보드 입력 : ")
# print("vc: ",vc)
# print("vc type: ",type(vc))
# print()

'''
입력받은 값을 원하는 형태의 자료형으로 사용하고 싶으면 형변환 해준다
'''

# dataA=input("숫자 입력_1 :")
# dataB=input("숫자 입력_2 :")
# # result = dataA + dataB # 그냥 이어서 나오게 된다. 고로 casting을 해서 형변환을 해줘야 한다.
# # print("result: ",result)

# dataA = int(dataA)
# dataB = int(dataB)
# result = dataA + dataB #int로 형변환을 했기 때문에 연산이 가능해진다.
# print("result : ", result)
# print()

# ia=int(input("첫번째 숫자 입력 > "))#이렇게 한번에 변환시킬 수 있다. 
# ib=int(input("두번째 숫자 입력 > "))#함수 안에서 함수를 호출할 수 있다.
# res = ia + ib
# print("{} + {} = {}". format(ia, ib, res))
# print()

# nation = "한국 kor"
# k,e = nation.split() #공백을 기준으로 문자열을 나눠준다. 그리고 이 나눠진 것을 두개의 변수에 담는다. 
# print(k)
# print(e) 
# print("{} , {}". format(k,e))

data = input("데이터 두개를 입력 > ")
print("data : ",data)
v1, v2 = data.split() #연속 입력해서 각각 데이터로 저장하려면 split을 눌러야 한다. 
print("v1 : {}, v2 : {}".format(v1,v2)) #input은 C의 scanf와 되게 비슷한 함수인 것 같다..!