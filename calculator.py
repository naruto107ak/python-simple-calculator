def calculator(a,b,c):
    if c==1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:
        return a/b
while True:
    a=int(input("enter first number:")) 
    b=int(input("enter second number:"))
    print("-----------enter 1 for addition-----------")
    print("-----------enter 2 for subtraction-----------")
    print("-----------enter 3 for multiplication-----------")
    print("-----------enter 4 for division-----------")
    c=int(input("enter your choice:"))
    print(calculator(a,b,c))
    choice=input("enter n to exit")
    if choice=="n":
        break    
print("thank you for using our service")