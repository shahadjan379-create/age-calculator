num1 = int(input("enter a number:"))
num2 = int(input("enter another number:"))
num3 = float(input("enter one moree:"))
if num1 < num2 and num3 < num2:
    print ("num2:",num2,"is the highest value")
elif num1 > num2 and num1 < num3:
    print ("num3:",num3,"is the higest value")
elif num1 < num2 and num2 > num3:
    print ("num2:",num2,"is the highest value")
elif  num1 == num2 == num3:
    print ("all values are equal")