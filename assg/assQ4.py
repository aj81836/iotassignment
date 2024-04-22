#Write a Python function to find the maximum of three numbers.
num1=int(input("Enter the first num1: "))
num2=int(input("Enter the second num2: "))
num3=int(input("Enter the third num3: "))

if num1==num2==num3:
    print("num1,num2 nad num3 are equal")
elif num1>num2:
     print("num1 is greater")
elif num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")
    