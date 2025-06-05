def equalornot(number1, number2):
    if(number1 ^ number2)!= 0:
        print("numbers are not equal")

    else:
        print("both numbers are equal")


number1 = int(input("enter the first number to compare"))
number2 = int(input("enter the second number"))
equalornot(number1,number2)