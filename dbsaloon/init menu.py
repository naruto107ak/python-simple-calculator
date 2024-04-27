import customers
import services
import employees
import users
while True:
    print("------------------------1customers----------------------------")
    print("-------------------------2services----------------------------")
    print("------------------------3employees----------------------------")
    print("-------------------------4users-------------------------------")
    ch=int(input("enter your choice:"))
    
    if ch==1:
        print("------------------------1insert----------------------------")
        print("-------------------------2delete----------------------------")
        print("------------------------3showall----------------------------")
        print("-------------------------4search-------------------------------")
        choice=int(input("enter your choice"))
        if choice==1:
            print(customers.insert())
        if choice==2:
            print(customers.delete())
        if choice==3:
            print(customers.showdata())
        if choice==4:
            print(customers.search())
    if ch==2:
        
        print("------------------------1insert----------------------------")
        print("-------------------------2delete----------------------------")
        print("------------------------3showall----------------------------")            
        print("-------------------------4search-------------------------------")
        choice=int(input("enter your choice"))
        if choice==1:
            print(services.insert())
        if choice==2:
            print(services.delete())
        if choice==3:
            print(services.showdata())
        if choice==4:
            print(services.search())
    if ch==3:
        
        print("------------------------1insert----------------------------")
        print("-------------------------2delete----------------------------")
        print("------------------------3showall----------------------------")
        print("-------------------------4search-------------------------------")
        choice=int(input("enter your choice"))
        if choice==1:
            print(employees.insert())
        if choice==2:
            print(employees.delete())
        if choice==3:
            print(employees.showdata())
        if choice==4:
            print(employees.search())
    if ch==4:
        
        print("------------------------1insert----------------------------")
        print("-------------------------2delete----------------------------")
        print("------------------------3showall----------------------------")
        print("-------------------------4search-------------------------------")
        choice=int(input("enter your choice"))
        if choice==1:
            print(users.insert())
        if choice==2:
            print(users.delete())
        if choice==3:
            print(users.showdata())
        if choice==4:
            print(users.search())
    exit=input("enter n to exit:")
    if exit=="n":
        break
      
    
    
