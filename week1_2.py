height = input("키를 입력해주세요(소수점 첫번쨰 자리까지) : ")
weight = input("체중을 입력해주세요(소수점 첫번째 자리까지) : ")
height = float(height)
weight = float(weight)
print("키 : ", height)
print("체중 : ", weight)

BMI = weight/(height*height)*10000

print("귀하의 BMI는", BMI,"입니다")

#print("18.5 이하는 저체중, 18.5 ~ 22.9 사이는 정상, 23.0 ~ 24.9 사이면 과체중, 25.0 이상은 비만")

if BMI <= 18.5:
    print("귀하는 저체중입니다.")
elif BMI <= 22.9:
    print("귀하는 정상입니다.")
elif BMI <= 24.9:
    print("귀하는 과체중입니다.")
elif BMI > 25.0:
    print("귀하는 비만입니다.")
