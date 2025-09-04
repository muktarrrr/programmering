print("hej,hur gammal är du ")
age = input()
age = int(age)

if age >= 15 and age <= 20:
    print("du ska ha ungdomsbiljet, 20kr tack")

elif age <= 14:
    print("barn biljet det är 16kr, tack")

elif age >= 65:
    print("senior biljet, det är 21kr, tack")

else:
    print("ordinarie biljet 27kr")
