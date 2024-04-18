#Write a program to accept a 4 digit number and
#a. Display face value of each decimal digit
#b. Display place value of each decimal digit
#c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
#ut should be



def face_value(num):
    

    if not isinstance(num, int) or not (1000 <= num <= 9999):
        face=int(input("Please enter a valid 4-digit integer."))

    thousands = num // 1000
    hundreds = (num % 1000) // 100
    tens = (num % 100) // 10
    ones = num % 10

    print("Face value of digits:")
    print(f"\tThousands digit: {thousands}")
    print(f"\tHundreds digit: {hundreds}")
    print(f"\tTens digit: {tens}")
    print(f"\tOnes digit: {ones}")

    print("\nPlace value of digits:")
    print(f"\tThousands digit: {thousands * 1000}")
    print(f"\tHundreds digit: {hundreds * 100}")
    print(f"\tTens digit: {tens * 10}")
    print(f"\tOnes digit: {ones * 1}")

    
    reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands
    print("\nNumber in place value:", reversed_number)


while True:
    try:
        face = int(input("Enter a 4-digit number: "))
        face_value(face)
        break  
    except int as e:
        print(e) 