try:
    a=int(input("enter no:"))
    operator=input("enter operator:(+,-,/,*)")
    b=int(input("enter no:"))
    if operator=="+":
        print(a+b)
    elif operator=="-":
        print(a-b)
    elif operator=="*":
        print(a*b)
    elif operator=="/":
        print(a/b)
    else:
        print("invalid input")
except:
    print("something went wrong")
finally:
    print(" Thanq Users for using my calculator ")