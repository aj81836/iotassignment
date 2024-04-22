#The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
#ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
#Average Grade
#90-100 A
#80-89 B
#70-79 C
#60-69 D
#0-59 F

math=int(input("Enter the math marks: "))
sci=int(input("Enter the sciences marks: "))
marathi=int(input("Enter the marathi marks: "))

average=(math+sci+marathi)/3
#print(f"average={average}")

if average>90:
    print("Grade A")
#elis average>80:
    print("Grade B")

print(f"average={average}")





