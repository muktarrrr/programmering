print("welcome")

number_1 = input()

try:
    number_1 = int(number_1)
except:
    print("Something went wrong")
    exit()

number_2 = input()

try:
    number_2 = int(number_2)
except:
    print("Something went wrong")
    exit()
    
def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division (x,y):
    if y == 0:
        print("Can't divide by zero") 
        exit()
    return x/y

print("what do you want to do ")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. divition")

choice = input("enter choice (1/2/3/4):")

if choice == "1":
    print("result:",addition(number_1, number_2))
elif choice == "2":    
    print("result:",subtraction (number_1, number_2))
elif choice == "3":
    print("result:", multiplication(number_1, number_2)) 
elif choice == "4":
    print("result:",division(number_1, number_2))
