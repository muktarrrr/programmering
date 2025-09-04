print("hej! hur gammal är du?")
age = input()
age = int(age)

if age <18:
    print("gu är ett barn")

elif age >=18 and age <60:
    print("du är vuxen")
elif age >=60:
    print("du är gammal")