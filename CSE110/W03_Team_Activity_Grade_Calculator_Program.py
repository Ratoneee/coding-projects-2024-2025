grade = int(input("What was your grade? "))

if grade >= 90:
    grade_letter = "A"
elif grade >= 80:
    grade_letter = "B"
elif grade >= 70:
    grade_letter = "C"
elif grade >= 60:
    grade_letter = "D"
else:
    grade_letter = "F"

print(f"your grade was {grade_letter}")

if grade >= 70:
    print("congrats! you pasted the class.")
else:
    print("you unfortunately did not pass the class.")