name=input("Enter student name:")
python_marks=float(input("Enter python marks:"))
maths_marks=float(input("Enter maths marks:"))
science_marks=float(input("Enter science marks:"))

total=python_marks+maths_marks+science_marks
average=total/3
print("\n---Student performance---")
print("Name:",name)
print("Python:",python_marks)
print("maths:",maths_marks)
print("science:",science_marks)
print("Total:",total)
print("Average:",average)

if average>=90:
    grade="A"
elif average>=75:
    grade="B"
elif average>=60:
    grade="C"
elif average>=40:
    grade="D"
else:
    grade="F"

print("Grade:",grade)
if python_marks>=40 and maths_marks>=40 and science_marks>=40:
    print("Result:PASS")
else:
    print("Result:FAIL")


