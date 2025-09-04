print("hej! välkommen till kiosk, ")
print("glass,varmkov,läsk,godis")

item = input()

if item == "glass":
    print("det är 20kr")
    print("Hur många vill du ha ?")
    amount= input()
    amount = int(amount)

    print("Det blir", amount * 20, "kr")
    
elif item == "varmkorv":
    print("det är 15")
    print("hur, många vill du ha?")
    amount = input()
    amount = int(amount)
    print("det blir", amount * 15,"kr")
elif item == "läsk":
    print("det är 15kr")
    print("hur, många vill du ha?")
    amount = input()
    amount= int(amount)
    print("det blir", amount * 15, "kr" )
elif item == "godis":
    print("hur många vill du ha?")
    amount = input()
    amount= int(amount)
    print("det blir", amount * 10, "kr")
    print("det är 10kr")

else:
    print(" out of stock") 


