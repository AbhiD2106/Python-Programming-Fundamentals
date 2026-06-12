
# switch case

a=int(input('enter number between 1 to 3:'))

match a:
    case 1:
        print("the value is 1:")
    case 2:
        print("the value is 2:")
    case 3:
        print("the value is 3:")
    case _:
        print("the value is default:")