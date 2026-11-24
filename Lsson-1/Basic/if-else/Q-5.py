n=int(input("Enter Your No:-"))
match n:
    case 1|2:
        print("low")
    case 3|4:
        print("medium")
    case 5|6:
        print("high")
    case _:
        print("Invalid")