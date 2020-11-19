




#Ex07_operator.py

'''
산술 연산자
'''
# va, vb = 5, 2
# print("{} + {} = {}".format(va,vb,va+vb)) #덧셈
# print("{} - {} = {}".format(va,vb,va-vb)) #뺄셈
# print("{} * {} = {}".format(va,vb,va*vb)) #곱셈
# print("{} / {} = {}".format(va,vb,va/vb)) #나눗셈
# print("{} % {} = {}".format(va,vb,va%vb)) #나머지
# print("{} // {} = {}".format(va,vb,va//vb)) #몫
# print("{} ** {} = {}".format(va,vb,va**vb)) #거듭제곱 ***은 세제곱 아니다. 2를 바꿔줘야 3제곱이 되던 뭐가 되던 한다. 


'''
복합 대입 연산자
+=, -=....
Ex) a += b -> a = a + b
  a와 b를 더해서 나온 결과를 a에 대입한다. 
-계산해서 나온 결과를 왼쪽에 대입하기 때문에, 왼쪽에는 항상 변수가 있어야 한다. 

'''
# vc = 5
# print("vc : ", vc)

# vc += 1
# print("vc += 1: ",vc)

# vc -= 2
# print("vc -= 2:", vc)

# vd = 2
# vd *= vc
# print("vd: ",vd)

'''
비교 연산자
- 두개의 데이터를 비교 할 때 사용한다.
    : < , > , <= , >=
    == 서로 같으면 참
    != 서로 다르면 참
- 비교해서 나온 결과를 True(참), False(거짓)으로 표시한다
'''
# ve, vf = 7, 9
# print("ve : {} - vf : {}".format(ve, vf))
# print()
# print("ve > 10 :", ve > 10)
# print("ve <= 10 :", ve <= 10) # <=이 순서로 꼭 적어준다. =<는 안된다.
# print("ve == 10 :", ve == 10)
# print("ve == vf : ", ve == vf)
# print("ve != vf :", ve != vf)


'''
논리 연산자
- and 연산 : 두개의 조건식이 모두 참일때 참이다.
    > 조건식_a and 조건식_b

- or 연산 : 두개의 조건식 중에서 하나라도 참이면 참이다. 
    > 조건식_a or 조건식_b

- not 연산 : 참은 거짓으로 , 거짓은 참으로 변경한다.
'''

# vg, vh = 10, 15
# print("vg : {} - vh : {}". format(vg,vh))
# print()
# print("vg > 10  and vh < 20 : ", vg > 10 and vh < 20)
# print("vg < 10  and vh < 20 : ", vg < 10 and vh < 20)
# print("vg <= 10  and vh < 20 : ", vg <= 10 and vh < 20)
# print()

# print("vg == 10 or vh > 20 : ", vg == 10 or vh >20)
# print("vg > 10 or vh > 20 : ", vg > 10 or vh >20)
# print()
# print("vg의 bool값은: ",bool(vg))
# print("not False : ", not False)
# print("not vg : ", not vg)


'''
식별 연산자
- 자료형을 확인하는 연산자
- type() is 자료형
    : type 안의 자료형이 is 뒤에 자료형과 같으면 참.

    type() is not 
    :type 안의 자료형이 is 뒤에 자료형과 다르면 참.
'''
# vi = 7
# print("vi : ", vi)
# print("type(vi) is int : ",type(vi) is int)
# print("type(vi) is int : ",type(vi) is not int)
# print("type(vi) is int : ",type(vi) is float)

'''
멤버 연산자
-n in ()
    > n의 값이 오른쪽에 ()안에 있으면 참.

-n not in ()
    > n의 값이 오른쪽 ()안에 없으면 참.
'''

vj = 5
print("vj : ", vj)
print("vj in (2,8,5) : ", vj in (2,8,5))
print("vj in (2,8,3) : ", vj in (2,8,3))
print("vj not in (2,8,5) : ", vj not in (2,8,5)) #python으로 짤 수 있는 알고리즘은 무궁무진하게 많이 있다..

