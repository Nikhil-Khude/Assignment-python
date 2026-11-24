a,b=map(int,input("Enter Your No:-").split())
print("1.Addition,2.Subtraction ,3.Multiplication ,4.Division, 5.Floor Division ,6.Modulus ,7.Exponentiation")
choice=int(input("Enter Your No:-"))
if choice==1:
    print("ADDITION",a+b)
elif choice==2:
    print("sutraction",a-b)
elif choice==3:
    print("Multiplication",a*b)
elif choice==4:
    print("Division",a/b)
elif choice==5:
    print("Floor Division",a//b)
elif choice==6:
    print("MOdules",a%b)
elif choice==7:
    print("Exponentiation",a**b)
else:
    print("Invalid Choice")
