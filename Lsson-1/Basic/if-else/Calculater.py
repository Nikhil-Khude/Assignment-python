a,b=map(int,input("entr Your Numbers:-").split())
choice=int(input("enter your choice:"))

match choice:
    case 1:
        print("Addition",a+b)
    case 2:
        print("subtractin",a-b)
    case 3:
        print("Multiplacation",a*b)
    case 4:
        print("Division",a/b)
    case _:
        print("Invalid Choice")